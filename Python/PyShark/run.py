from tkinter import *
from pyshark.frontend.frontend_sniffer import AppWindow

window = Tk()

myApp = AppWindow(window)
myApp.add_buttons()
myApp.add_text_box()

window.title("PyShark Packet Sniffer")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()
