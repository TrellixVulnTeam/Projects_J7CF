import threading
import tkinter as tk
from tkinter import ttk
from pyshark.backend.sniffer2 import Run


class AppWindow(object):
    def __init__(self, window):
        self.runner = Run()
        self.thread_running = bool
        self.json_data = []

        self.master_frame = tk.Frame(window, bg="Light Blue", bd=3, relief=tk.RIDGE)
        self.master_frame.grid(sticky=tk.NSEW)
        self.master_frame.grid_columnconfigure(0, weight=1)
        self.master_frame.grid_rowconfigure(3, weight=1)

    def add_filter_fields(self):
        filter_frame = tk.Frame(self.master_frame, bg="Light Blue")
        filter_frame.grid(row=1, column=0, sticky=tk.EW)

    def add_buttons(self):
        button_frame = tk.Frame(self.master_frame, bg="Light Blue")
        button_frame.grid(row=2, column=0, sticky=tk.NSEW)
        b_run = tk.Button(button_frame, text="Run sniffing", width=12, command=self.run_button)
        b_run.grid(row=2, column=0, padx=5)
        b_stop = tk.Button(button_frame, text="Stop", width=12, command=self.stop_button)
        b_stop.grid(row=2, column=1, padx=5)
        b_clear = tk.Button(button_frame, text="Clear ", width=12, command=self.clr_button)
        b_clear.grid(row=2, column=2, padx=5)

        button_frame.grid_rowconfigure(2, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

    def add_text_box(self):

        # boxframe = tk.Frame(self.master_frame, bg="Red")
        # boxframe.grid(row=3, column=0, sticky=tk.NSEW)
        # box = tk.Listbox(boxframe)
        # box.grid(row=0, column=0, sticky=tk.NSEW)
        # boxframe.grid_rowconfigure(0, weight=1)
        # boxframe.grid_columnconfigure(0, weight=1)

        scroll_frame = tk.Frame(self.master_frame)
        scroll_frame.grid(row=3, column=0, sticky=tk.NSEW)

        self.text_box = tk.ttk.Treeview(scroll_frame)
        self.text_box.grid(row=0, column=0, sticky=tk.NSEW)
        scroll_frame.grid_rowconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(0, weight=1)

        self.text_box["columns"] = (1, 2, 3, 4, 5, 6)
        self.text_box.column("#0", width=150, minwidth=90, stretch=tk.NO)
        self.text_box.column(1, width=150, minwidth=150, stretch=tk.NO)
        self.text_box.column(2, width=200, minwidth=200, stretch=tk.NO)
        self.text_box.column(3, width=200, minwidth=50, stretch=tk.NO)
        self.text_box.column(4, width=80, minwidth=50, stretch=tk.NO)
        self.text_box.column(5, width=80, minwidth=50, stretch=tk.NO)
        self.text_box.column(6, width=300, minwidth=150, stretch=tk.YES)

        self.text_box.heading("#0", text="No.", anchor=tk.W)
        self.text_box.heading(1, text="Time", anchor=tk.W)
        self.text_box.heading(2, text="Source", anchor=tk.W)
        self.text_box.heading(3, text="Destination", anchor=tk.W)
        self.text_box.heading(4, text="Protocol", anchor=tk.W)
        self.text_box.heading(5, text="Length", anchor=tk.W)
        self.text_box.heading(6, text="Info", anchor=tk.W)

        scrollbar_y = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL)
        scrollbar_y.config(command=self.text_box.yview)
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)
        self.text_box.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = tk.Scrollbar(scroll_frame, orient=tk.HORIZONTAL)
        scrollbar_x.config(command=self.text_box.xview)
        scrollbar_x.grid(row=1, column=0, sticky=tk.EW)
        self.text_box.configure(xscrollcommand=scrollbar_x.set)

        # scroll_frame.grid_rowconfigure(0, weight=1)
        # scroll_frame.grid_rowconfigure(1, weight=1)
        # scroll_frame.grid_rowconfigure(3, weight=1)
        # scroll_frame.grid_columnconfigure(0, weight=1)
        # scroll_frame.grid_columnconfigure(1, weight=1)

    def run_button(self):
        self.runner.thread_kill = True
        self.thread_print = threading.Thread(target=self.print_data)
        self.thread_print.start()

    def stop_button(self):
        print("Stopped")
        self.runner.thread_kill = False

    def print_data(self):
        while self.runner.thread_kill:
            for row in self.runner.run().items():
                # print(row[1])

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
                    ether_frame = self.text_box.insert("", i, "", text="Frame [{}]".format(i),
                                                       values=(
                                                           time, ipv4_src, ipv4_dst, protocol, header,
                                                           "TTL = {} Version: {}".format(ttl, version)))
                    self.text_box.insert(ether_frame, "end", "", text="MAC",
                                         values=("", mac_src, mac_dst, mac_proto))

                    self.text_box.insert(ether_frame, "end", "", text="Data",
                                         values=("", data))

                    if protocol == 6:
                        tcp_src = row[1].get('TCP').get('Source')
                        tcp_dst = row[1].get('TCP').get('Dest')
                        self.text_box.insert(ether_frame, "end", "", text="Transport Protocol",
                                             values=("", (":", tcp_src), (":", tcp_dst), "TCP"))
                    elif protocol == 17:
                        udp_src = row[1].get('UDP').get('Source')
                        udp_dst = row[1].get('UDP').get('Dest')
                        self.text_box.insert(ether_frame, "end", "", text="Transport Protocol",
                                             values=("", (":", udp_src), (":", udp_dst), "UDP"))

    def clr_button(self):
        self.text_box.delete(*self.text_box.get_children())
