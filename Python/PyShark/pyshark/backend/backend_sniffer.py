import socket
import tkinter
import textwrap
from datetime import datetime as dt
from pyshark.backend.unpack_ethernet import Ethernet
from pyshark.backend.unpack_packet_ipv4 import IPv4
from pyshark.backend.unpack_icmp_seg import ICMP
from pyshark.backend.unpack_udp_seg import UDP
from pyshark.backend.unpack_tcp_seg import TCP

# frame counter
i = 0


class Sniff:

    def __init__(self):
        self.conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        self.thread_kill = True
        self.json_data = []

    def run_sniff(self):
        global i

        while self.thread_kill:
            raw_data, addr = self.conn.recvfrom(65536)
            eth = Ethernet(raw_data)
            frame_time = "{}:{}:{}.{}".format(dt.now().time().hour, dt.now().minute, dt.now().second,
                                              str(dt.now().microsecond)[:3])
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


class Insert:

    @staticmethod
    def unpack_and_insert(row, text_box, thread_kill0):

        if thread_kill0:
            i = row[1].get('FrameCnt')
            time = row[1].get('Time')
            data = row[1].get('Data')
            if row[1].get('IPv4') is not None:
                ipv4_src = row[1].get('IPv4').get('Source')
                ipv4_dst = row[1].get('IPv4').get('Dest')
                ttl = row[1].get('IPv4').get('TTL')
                protocol = row[1].get('IPv4').get('Protocol')
                version = row[1].get('IPv4').get('Version')
                header = row[1].get('IPv4').get('Header')

                mac_src = row[1].get('MAC').get('Source')
                mac_dst = row[1].get('MAC').get('Dest')
                mac_proto = row[1].get('MAC').get('Protocol')

                # Level 1
                ether_frame = text_box.insert("", i, "", text="Frame [{}]".format(i),
                                              values=(
                                                  time, ipv4_src, ipv4_dst, protocol, header,
                                                  "TTL = {} Version: {}".format(ttl, version)), tags='eth_tag')
                text_box.insert(ether_frame, "end", "", text="MAC",
                                values=("", mac_src, mac_dst, mac_proto), tags='mac_tag')

                if protocol == 6:
                    tcp_src = row[1].get('TCP').get('Source')
                    tcp_dst = row[1].get('TCP').get('Dest')
                    text_box.insert(ether_frame, "end", "", text="Transport Protocol",
                                    values=("", (":", tcp_src), (":", tcp_dst), "TCP"), tags='tcp_tag')
                elif protocol == 17:
                    udp_src = row[1].get('UDP').get('Source')
                    udp_dst = row[1].get('UDP').get('Dest')
                    text_box.insert(ether_frame, "end", "", text="Transport Protocol",
                                    values=("", (":", udp_src), (":", udp_dst), "UDP"), tags='udp_tag')

                elif protocol == 1:
                    icmp_type = row[1].get('ICMP').get('Type')
                    icmp_code = row[1].get('ICMP').get('Code')
                    icmp_chksum = row[1].get('ICMP').get('Checksum')
                    text_box.insert(ether_frame, "end", "", text="Transport Protocol",
                                    values=(
                                        ("", ("Type: {}".format(icmp_type)),
                                         ("Code: {}".format(icmp_code)),
                                         "ICMP", "Checksum: {}".format(icmp_chksum))), tags='icmp_tag')

                if len(data) > 0:
                    data_row = text_box.insert(ether_frame, "end", "", text="Data", tags='data_tag')
                    data = str(data)
                    wrapped_data = textwrap.wrap(data, 50)

                    for row_data in wrapped_data:
                        try:
                            text_box.insert(data_row, "end", "",
                                            values=(row_data, "", "", "", "", "",), tags='data_tag2')
                        except tkinter.TclError:
                            pass

                text_box.tag_configure('data_tag', background='Light Grey')
