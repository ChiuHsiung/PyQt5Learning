# -*- coding: utf-8 -*-
# Ex3_MessageBox.py created by zhuangqiuxiong on 2017/1/6.
__author__ = 'zhuangqiuxiong'

import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from Example.Ex2_ButtonAndToolTip import WidgetCreator

class WidgetCreator_CloseEvent(WidgetCreator):

    #overwrite
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = WidgetCreator_CloseEvent()
    w.setFrame(300, 300, 500, 300)
    w.setTitle('Message Box')

    w.show()

    sys.exit(app.exec_())

