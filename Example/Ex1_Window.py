# -*- coding: utf-8 -*-
# Ex1_Window.py created by zhuangqiuxiong on 2017/1/6.
__author__ = 'zhuangqiuxiong'

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == "__main__":

    #Every PyQt5 application must create an application object.
    app = QApplication(sys.argv)

    #The QWidget widget is the base class of all user interface object in PyQt5.
    #A widget with no params is called a window.
    w = QWidget()

    # w.resize(250, 150)
    # w.move(300, 300)
    # It locates the window on the screen and sets its size.
    w.setGeometry(300, 300, 250, 150)
    w.setWindowTitle('Simple Window')

    w.setWindowIcon(QIcon('image/new-logo.png'))

    w.show()

    #The mainloop ends if we call exit() method or the main widget is destroyed.
    sys.exit(app.exec_())