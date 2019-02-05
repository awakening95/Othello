import time
import socket
import json
from src.board import *
from PyQt5.QtCore import *
from src.util import *


class Network(QThread):
    server_msg = pyqtSignal(dict)

    def __init__(self, sock):
        QThread.__init__(self)
        self.sock = sock

    def run(self):
        while True:
            msg = deserialize(self.sock)
            self.server_msg.emit(msg)
