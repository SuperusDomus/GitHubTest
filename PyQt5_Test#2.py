#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a quit
button. When we press the button,
the application terminates.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
import NodeClass as NC

def loadNodeGUI():
    retNode = NC.loadNode(0)
    print("Sucess\n")

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)

        qlbtn = QPushButton('Load node', self)
        qlbtn.clicked.connect(loadNodeGUI)
        qlbtn.resize(qlbtn .sizeHint())
        qlbtn.move(30, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    nodenr1 = NC.nodeCls()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())