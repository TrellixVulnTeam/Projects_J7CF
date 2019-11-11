import socket
import json
from pyshark.backend.unpack_ethernet import Ethernet
from pyshark.backend.unpack_packet_ipv4 import IPv4
from pyshark.backend.unpack_icmp_seg import ICMP
from pyshark.backend.unpack_udp_seg import UDP
from pyshark.backend.unpack_tcp_seg import TCP

from pyshark.backend.basic_functions import format_multi_line

TAB_1 = '\t  -  '
TAB_2 = '\t\t  -  '
TAB_3 = '\t\t\t  -  '
TAB_4 = '\t\t\t\t  -  '

DATA_TAB_1 = '\t '
DATA_TAB_2 = '\t\t '
DATA_TAB_3 = '\t\t\t '
DATA_TAB_4 = '\t\t\t\t '


class Run:
    def __init__(self):
        self.conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        self.thread_kill = True
        self.json_data_l2 = {"Ethernet": {"MAC": {"Dest": "", "Source": "", "Protocol": ""},
                                          "IPv4": {"Dest": "", "Source": "", "Protocol": "", "Version": "",
                                                   "Header": "", "TTL": ""},
                                          "TCP": {"Dest": "", "Source": "", "SEQ": "", "ACKN": "", "FLAGS": ""},
                                          "UDP": {"Dest": "", "Source": "", "Size": ""}}}
        self.frame_counter = 0

    def run(self):

        while self.thread_kill:

            raw_data, addr = self.conn.recvfrom(65536)
            eth = Ethernet(raw_data)
            self.frame_counter += 1

            print(
                '\n========================================================================================================='
                '====================================')
            print('\nEthernet Frame [{}]:'.format(self.frame_counter))
            print(TAB_1 + 'Destination MAC Address: {}, Source MAC Address: {}, Ethernet Protocol: {}'.format(
                eth.dest_mac,
                eth.src_mac,
                eth.proto))

            # eth proto == 8 then its IPv4
            if eth.proto == 8:
                ipv4 = IPv4(eth.data)

                print(DATA_TAB_1 + 'IPv4 Packet:')
                print(
                    TAB_2 + 'Destination IP Address: {}, Source IP Address: {}, Internet Protocol: {}, Version: {},'
                            ' Header: {}, TTL: {} '.format(ipv4.dest, ipv4.src, ipv4.ip_proto, ipv4.ver,
                                                           ipv4.header,
                                                           ipv4.ttl))
                # ip proto == 6 then its TCP
                if ipv4.ip_proto == 6 and len(ipv4.data) > 13:
                    tcp = TCP(ipv4.data)

                    print(DATA_TAB_2 + 'TCP Segment:')
                    print(TAB_3 + 'Destination Port: {}, Source Port: {}, Sequence: {}, Acknowledge: {},'.format(
                        tcp.dest_port,
                        tcp.src_port,
                        tcp.sequence,
                        tcp.acknowledge))
                    print(TAB_3 + 'Flags: URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {} '.format(
                        tcp.flag_urg, tcp.flag_ack,
                        tcp.flag_psh,
                        tcp.flag_rst, tcp.flag_syn,
                        tcp.flag_fin))
                    print(TAB_3 + 'Data:')
                    print(format_multi_line(DATA_TAB_3, tcp.data))

                # ip proto == 17 then its UDP
                elif ipv4.ip_proto == 17 and len(ipv4.data) > 7:
                    udp = UDP(ipv4.data)

                    print(DATA_TAB_2 + 'UDP Segment:')
                    print(TAB_3 + 'Destination Port: {}, Source Port: {}, Size: {}'.format(udp.dest_port,
                                                                                           udp.src_port,
                                                                                           udp.size))
                    print(TAB_3 + 'Data:')
                    print(format_multi_line(DATA_TAB_2, udp.data))

                # ip proto == 1 then its ICMP
                elif ipv4.ip_proto == 1 and len(ipv4.data) > 3:
                    icmp = ICMP(ipv4.data)

                    print(DATA_TAB_2 + 'ICMP Segment:')
                    print(TAB_3 + 'ICMP type: {}, Code: {}, Checksum: {}'.format(icmp.icmp_type, icmp.code,
                                                                                 icmp.checksum))
                    print(format_multi_line(DATA_TAB_3, icmp.data))
                else:
                    print(TAB_1 + 'Data:')
                    print(format_multi_line(DATA_TAB_2, ipv4.data))

    def __del__(self):
        print("Stopped")
