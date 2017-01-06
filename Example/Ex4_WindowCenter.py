# -*- coding: utf-8 -*-
# Ex4_WindowCenter.py created by zhuangqiuxiong on 2017/1/6.
__author__ = 'zhuangqiuxiong'

import sys

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

from PyQt5.QtCore import QRect

from Example.Ex2_ButtonAndToolTip import WidgetCreator

class WidgetCreator_Center(WidgetCreator):

    def moveToScreenCenter(self):

        #Get the frame of widget
        frame = self.frameGeometry()

        #Get the center of screen widget
        screenFrame = QDesktopWidget().availableGeometry()

        frame.moveCenter(screenFrame.center())

        self.move(frame.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = WidgetCreator_Center()
    w.setFrame(300, 300, 500, 300)
    w.setTitle('Message Box')

    w.moveToScreenCenter()

    w.show()

    sys.exit(app.exec_())