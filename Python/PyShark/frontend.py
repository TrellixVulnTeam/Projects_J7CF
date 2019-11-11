import threading
import tkinter as tk
from tkinter import ttk
from pyshark.backend.backend_sniffer import Sniff, unpack_and_insert


class AppWindow(object):
    def __init__(self, window):
        self.sniffed = Sniff()
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
        b_run = tk.Button(button_frame, text="Run sniffing", width=12, command=self.sniff_button, font=("Courier", 15))
        b_run.grid(row=2, column=0, padx=5)
        b_stop = tk.Button(button_frame, text="Stop", width=12, command=self.stop_button, font=("Courier", 15))
        b_stop.grid(row=2, column=1, padx=5)
        b_clear = tk.Button(button_frame, text="Clear ", width=12, command=self.clr_button, font=("Courier", 15))
        b_clear.grid(row=2, column=2, padx=5)
        b_quit = tk.Button(button_frame, text="Quit", width=12, command=self.quit_button, font=("Courier", 15))
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
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Courier", 12), rowheight=40)
        style.configure("Treeview.Heading", font=("Courier", 15))

        scroll_frame.grid_rowconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(0, weight=1)

        self.text_box["columns"] = (1, 2, 3, 4, 5, 6)
        self.text_box.column("#0", width=390, minwidth=90, stretch=tk.NO)
        self.text_box.column(1, width=300, minwidth=150, stretch=tk.NO)
        self.text_box.column(2, width=350, minwidth=200, stretch=tk.NO)
        self.text_box.column(3, width=350, minwidth=50, stretch=tk.NO)
        self.text_box.column(4, width=280, minwidth=50, stretch=tk.NO)
        self.text_box.column(5, width=220, minwidth=90, stretch=tk.NO)
        self.text_box.column(6, width=300, minwidth=150, stretch=tk.YES)

        self.text_box.heading("#0", text="No.", anchor=tk.W)
        self.text_box.heading(1, text="Time", anchor=tk.W)
        self.text_box.heading(2, text="Source", anchor=tk.W)
        self.text_box.heading(3, text="Destination", anchor=tk.W)
        self.text_box.heading(4, text="Protocol", anchor=tk.W)
        self.text_box.heading(5, text="Length", anchor=tk.W)
        self.text_box.heading(6, text="Info", anchor=tk.W)

        scrollbar_y = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, width=25)
        scrollbar_y.config(command=self.text_box.yview)
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)
        self.text_box.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = tk.Scrollbar(scroll_frame, orient=tk.HORIZONTAL, width=25)
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
            for row in self.sniffed.run().items():
                unpack_and_insert(row, self.text_box)

    def clr_button(self):
        self.text_box.delete(*self.text_box.get_children())

    def quit_button(self):
        self.master_frame.quit()
