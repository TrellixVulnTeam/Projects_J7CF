import sys
from PyQt5.QtWidgets import QApplication
from calc import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.setFixedSize(460, 240)
sys.exit(app.exec_())
