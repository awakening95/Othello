import sys
from src.board import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # ui = Ui_MainWindow("113.30.24.43")
    ui = Ui_MainWindow("192.168.43.186")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
