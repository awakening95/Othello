import sys
from src.board import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow("127.0.0.1")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
