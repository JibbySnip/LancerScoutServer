#!/usr/bin/env python3
import requests, tba, sys
from scenes.homescreen import HomeScreen
from scenes import page_window
# from scenes.matches_view import MatchScreen
from PyQt5 import QtCore, QtGui, QtWidgets


# def find_event_key(team):

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
          super().__init__(parent)

          self.stacked_widget = QtWidgets.QStackedWidget()
          self.setCentralWidget(self.stacked_widget)

          self.m_pages = {}

          self.register(HomeScreen(), "homescreen")
          # self.register(MatchScreen(), "matches_view")

          self.goto("homescreen")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, page_window.PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
