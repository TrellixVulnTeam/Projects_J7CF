import socket
import time
from datetime import datetime as dt
from pyshark.backend.unpack_ethernet import Ethernet
from pyshark.backend.unpack_packet_ipv4 import IPv4
from pyshark.backend.unpack_icmp_seg import ICMP
from pyshark.backend.unpack_udp_seg import UDP
from pyshark.backend.unpack_tcp_seg import TCP

TAB_1 = '\t  -  '
TAB_2 = '\t\t  -  '
TAB_3 = '\t\t\t  -  '
TAB_4 = '\t\t\t\t  -  '

DATA_TAB_1 = '\t '
DATA_TAB_2 = '\t\t '
DATA_TAB_3 = '\t\t\t '
DATA_TAB_4 = '\t\t\t\t '
# frame counter
i = 0


class Run:

    def __init__(self):
        self.conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        self.thread_kill = True
        self.json_data = []

    def run(self):
        global i

        while self.thread_kill:
            raw_data, addr = self.conn.recvfrom(65536)
            eth = Ethernet(raw_data)
            frame_time = "{}:{}:{}.{}".format(dt.now().time().hour, dt.now().minute, dt.now().second,
                                              dt.now().microsecond)
            self.json_data.append({"Ethernet": {"FrameCnt": i,
                                                "Time": "",
                                                "MAC": {"Dest": "", "Source": "", "Protocol": ""}}})

            self.json_data[i]["Ethernet"]["MAC"]["Dest"] = eth.dest_mac
            self.json_data[i]["Ethernet"]["MAC"]["Source"] = eth.src_mac
            self.json_data[i]["Ethernet"]["MAC"]["Protocol"] = eth.proto
            self.json_data[i]["Ethernet"]["Time"] = frame_time

            # eth proto == 8 then its IPv4
            if eth.proto == 8:
                ipv4 = IPv4(eth.data)
                self.json_data[i]["Ethernet"].update({
                    "IPv4": {"Dest": "", "Source": "", "Protocol": "", "Version": "",
                             "Header": "", "TTL": ""}})

                self.json_data[i]["Ethernet"]["IPv4"]["Dest"] = ipv4.dest
                self.json_data[i]["Ethernet"]["IPv4"]["Source"] = ipv4.src
                self.json_data[i]["Ethernet"]["IPv4"]["Protocol"] = ipv4.ip_proto
                self.json_data[i]["Ethernet"]["IPv4"]["TTL"] = ipv4.ttl
                self.json_data[i]["Ethernet"]["IPv4"]["Header"] = ipv4.header
                self.json_data[i]["Ethernet"]["IPv4"]["Version"] = ipv4.ver

                # ip proto == 6 then its TCP
                if ipv4.ip_proto == 6 and len(ipv4.data) > 13:
                    tcp = TCP(ipv4.data)

                    self.json_data[i]["Ethernet"].update({
                        "TCP": {"Dest": "", "Source": "", "SEQ": "", "ACKN": "",
                                "FLAGS": {"URG": "", "ACK": "", "PSH": "", "RST": "", "SYN": "",
                                          'FIN': ""}},
                        "Data": ""})

                    self.json_data[i]["Ethernet"]["TCP"]["SEQ"] = tcp.sequence
                    self.json_data[i]["Ethernet"]["TCP"]["ACKN"] = tcp.acknowledge
                    self.json_data[i]["Ethernet"]["TCP"]["Source"] = tcp.src_port
                    self.json_data[i]["Ethernet"]["TCP"]["Dest"] = tcp.dest_port
                    self.json_data[i]["Ethernet"]["TCP"]["FLAGS"]["FIN"] = tcp.flag_fin
                    self.json_data[i]["Ethernet"]["TCP"]["FLAGS"]["ACK"] = tcp.flag_ack
                    self.json_data[i]["Ethernet"]["TCP"]["FLAGS"]["SYN"] = tcp.flag_syn
                    self.json_data[i]["Ethernet"]["TCP"]["FLAGS"]["RST"] = tcp.flag_rst
                    self.json_data[i]["Ethernet"]["TCP"]["FLAGS"]["PSH"] = tcp.flag_psh
                    self.json_data[i]["Ethernet"]["TCP"]["FLAGS"]["URG"] = tcp.flag_urg
                    self.json_data[i]["Ethernet"]["Data"] = tcp.data


                # ip proto == 17 then its UDP
                elif ipv4.ip_proto == 17 and len(ipv4.data) > 7:
                    udp = UDP(ipv4.data)

                    self.json_data[i]["Ethernet"].update({
                        "UDP": {"Dest": "", "Source": "", "Size": ""},
                        "Data": ""})

                    self.json_data[i]["Ethernet"]["UDP"]["Size"] = udp.size
                    self.json_data[i]["Ethernet"]["UDP"]["Source"] = udp.src_port
                    self.json_data[i]["Ethernet"]["UDP"]["Dest"] = udp.dest_port
                    self.json_data[i]["Ethernet"]["Data"] = udp.data




                # ip proto == 1 then its ICMP
                elif ipv4.ip_proto == 1 and len(ipv4.data) > 3:
                    icmp = ICMP(ipv4.data)
                    self.json_data[i]["Ethernet"].update({
                        "ICMP": {"Type": "", "Code": "", "Checksum": ""},
                        "Data": ""})

                    self.json_data[i]["Ethernet"]["ICMP"]["Type"] = icmp.icmp_type
                    self.json_data[i]["Ethernet"]["ICMP"]["Code"] = icmp.code
                    self.json_data[i]["Ethernet"]["ICMP"]["Checksum"] = icmp.checksum
                    self.json_data[i]["Ethernet"]["Data"] = icmp.data

                else:
                    self.json_data[i]["Ethernet"].update({
                        "Data": ""})
                    self.json_data[i]["Ethernet"]["Data"] = ipv4.data

            i += 1
            return self.json_data[i - 1]

    def __del__(self):
        print("Stopped")
