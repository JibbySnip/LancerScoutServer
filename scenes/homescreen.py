from PyQt5 import QtCore, QtGui, QtWidgets
from scenes.page_window import PageWindow

class HomeScreen(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setWindowTitle("LancerScout")

    def initUi(self):
        self.addUiComponents()

    def addUiComponents(self):
        self.title_label = QtWidgets.QLabel("LancerScout", alignment = QtCore.Qt.AlignVCenter)
        self.title_label.setFont(QtGui.QFont("Courier New", 48))
