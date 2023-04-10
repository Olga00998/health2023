from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QNBoxLayout, QGridLayout,
                             QGroupBox, QRadioButton, QPushButton, QLabel,
                             QList Widget, QLineEdit)
from instr import *

class FinalWin(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    self.set_appear()
    self.show()
  def initUI():
    self.wotkh_text = QLabel(txt_workheart)
    self.index_text = QLabel(txt_index)
    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.index_text, allignment = Qt.AlignCenter)
    self.layout_line.addWidget(self.workh_text, allignment = Qt.AlignCenter)
    self.setLayout(self.layout_line)
  def set_appear(self):
    self.setWindowTitle(txt_finalwin)
    self.reasize(win_widgth, win_height)
    self.move(win_x, win_y)
