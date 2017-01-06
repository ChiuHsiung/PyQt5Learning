# -*- coding: utf-8 -*-
# Ex2_ButtonAndToolTip.py created by zhuangqiuxiong on 2017/1/6.
__author__ = 'zhuangqiuxiong'

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip

from PyQt5.QtGui import QFont, QIcon

from PyQt5.QtCore import QCoreApplication

class WidgetCreator(QWidget):

    def __init__(self):
        QWidget.__init__(self)

    def setFrame(self, *args):
        self.setGeometry(args[0], args[1], args[2], args[3])

    def setTitle(self, title: str):
        self.setWindowTitle(title)

    def setWindowIcon(self, imagePath: str):
        self.setWindowIcon(QIcon(imagePath))

    def showWindow(self):
        self.show()

    def addButton(self, buttonX: int, buttonY: int, buttonTitle: str, isNeedToolTip: bool, toolTipStr = None) -> QPushButton:
        btn = QPushButton(buttonTitle, self)
        btn.resize(btn.sizeHint())  #The sizeHint() method gives a recommended size for the button.
        btn.move(buttonX, buttonY)

        if isNeedToolTip:
            QToolTip.setFont(QFont('SansSerif', 10))
            btn.setToolTip(toolTipStr)

        return btn




def printText():
    print("Hello World")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = WidgetCreator()
    w.setFrame(300, 300, 500, 300)
    w.setTitle('Button and ToolTip')

    printBtn = w.addButton(50, 50, 'Print', True, 'This is a <b>QPushButton</b> widget')
    printBtn.clicked.connect(printText)

    exitBtn = w.addButton(200, 50, 'Exit', False)
    exitBtn.clicked.connect(QCoreApplication.instance().quit)

    w.show()

    sys.exit(app.exec_())