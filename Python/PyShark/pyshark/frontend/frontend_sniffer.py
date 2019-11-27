import threading
import tkinter as tk
from tkinter import ttk
from pyshark.backend.backend_sniffer import Sniff, Insert


class AppWindow(object):
    def __init__(self, window):
        self.sniffed = Sniff()
        self.insert = Insert()
        self.thread_running = bool
        self.json_data = []

        self.master_frame = tk.Frame(window, bg="gray13", bd=3, relief=tk.RIDGE)
        self.master_frame.grid(sticky=tk.NSEW)
        self.master_frame.grid_columnconfigure(0, weight=1)
        self.master_frame.grid_rowconfigure(3, weight=1)

    def add_filter_fields(self):
        filter_frame = tk.Frame(self.master_frame, bg="gray13")
        filter_frame.grid(row=1, column=0, sticky=tk.EW)

    def add_buttons(self):
        button_frame = tk.Frame(self.master_frame, bg="gray13")
        button_frame.grid(row=2, column=0, sticky=tk.NSEW)
        b_run = tk.Button(button_frame, text="Run sniffing", width=12, command=self.sniff_button, font=("Courier", 12),
                          bg="grey13", foreground="gray99")
        b_run.grid(row=2, column=0, padx=5)
        b_stop = tk.Button(button_frame, text="Stop", width=12, command=self.stop_button, font=("Courier", 12),
                           bg="grey13", foreground="gray99")
        b_stop.grid(row=2, column=1, padx=5)
        b_clear = tk.Button(button_frame, text="Clear ", width=12, command=self.clr_button, font=("Courier", 12),
                            bg="grey13", foreground="gray99")
        b_clear.grid(row=2, column=2, padx=5)
        b_quit = tk.Button(button_frame, text="Quit", width=12, command=self.quit_button, font=("Courier", 12),
                           bg="grey13", foreground="gray99")
        b_quit.grid(row=2, column=3, padx=5)

        button_frame.grid_rowconfigure(2, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

    def add_text_box(self):

        scroll_frame = tk.Frame(self.master_frame)
        scroll_frame.grid(row=3, column=0, sticky=tk.NSEW)

        self.text_box = tk.ttk.Treeview(scroll_frame)
        self.text_box.grid(row=0, column=0, sticky=tk.NSEW)

        style = tk.ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Courier", 12), foreground="gray99", rowheight=22,
                        bg="gray13", fieldbackground="gray13", highlightcolor="gray13")
        style.configure("Treeview.Heading", font=("Courier", 15), background="gray35", foreground="gray1",
                        relief="flat", highlightcolor="gray13")

        scroll_frame.grid_rowconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(0, weight=1)

        self.text_box["columns"] = (1, 2, 3, 4, 5, 6)
        self.text_box.column("#0", width=390, minwidth=90, stretch=tk.NO)
        self.text_box.column(1, width=200, minwidth=150, stretch=tk.NO)
        self.text_box.column(2, width=200, minwidth=200, stretch=tk.NO)
        self.text_box.column(3, width=200, minwidth=50, stretch=tk.NO)
        self.text_box.column(4, width=200, minwidth=50, stretch=tk.NO)
        self.text_box.column(5, width=200, minwidth=90, stretch=tk.NO)
        self.text_box.column(6, width=300, minwidth=150, stretch=tk.YES)

        self.text_box.heading("#0", text="|No.", anchor=tk.W)
        self.text_box.heading(1, text="|Time", anchor=tk.W)
        self.text_box.heading(2, text="|Source", anchor=tk.W)
        self.text_box.heading(3, text="|Destination", anchor=tk.W)
        self.text_box.heading(4, text="|Protocol", anchor=tk.W)
        self.text_box.heading(5, text="|Length", anchor=tk.W)
        self.text_box.heading(6, text="|Info", anchor=tk.W)

        scrollbar_y = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, width=15, bg="gray13")
        scrollbar_y.config(command=self.text_box.yview)
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)
        self.text_box.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = tk.Scrollbar(scroll_frame, orient=tk.HORIZONTAL, width=15, bg="gray13")
        scrollbar_x.config(command=self.text_box.xview)
        scrollbar_x.grid(row=1, column=0, sticky=tk.EW)
        self.text_box.configure(xscrollcommand=scrollbar_x.set)

    def sniff_button(self):
        self.sniffed.thread_kill = True
        self.thread_print = threading.Thread(target=self.print_data)
        self.thread_print.start()

    def stop_button(self):
        self.sniffed.thread_kill = False

    def print_data(self):
        while self.sniffed.thread_kill:
            for row in self.sniffed.run_sniff().items():
                self.insert.unpack_and_insert(row, self.text_box, self.sniffed.thread_kill)

    def clr_button(self):
        self.text_box.delete(*self.text_box.get_children())

    def quit_button(self):
        self.master_frame.quit()
