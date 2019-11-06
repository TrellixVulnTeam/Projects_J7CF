from tkinter import *
from main import AppWindow

window = Tk()
myApp = AppWindow(window)
window.title("PyShark Packet Sniffer")
myApp.add_buttons()
myApp.add_text_box()
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()
