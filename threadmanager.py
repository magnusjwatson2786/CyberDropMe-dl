
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def addthread(self):
    sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
    sizePolicy2.setHorizontalStretch(0)
    sizePolicy2.setVerticalStretch(0)
    sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    self.thread_n.append(QLabel(self.ui.groupBox))
    self.thread_n[-1].setSizePolicy(sizePolicy2)
    self.thread_n[-1].setMaximumSize(QSize(16777215, 20))
    self.ui.verticalLayout_3.addWidget(self.thread_n[-1])
    self.thread_n[-1].setText("name")

    self.thread_p.append(QLabel(self.ui.groupBox))
    self.thread_p[-1].setSizePolicy(sizePolicy1)
    self.thread_p[-1].setMinimumSize(QSize(40, 20))
    self.thread_p[-1].setMaximumSize(QSize(40, 20))
    self.ui.verticalLayout_4.addWidget(self.thread_p[-1])
    self.thread_p[-1].setText("12")


    