from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Dlitem():
    def __init__(self,link,size,parent):
        self.link = link
        # self.lidx=lidx
        self.flen=size
        self.csize=512*1024
        self.dlen=0
        self.strt=0
        self.filename="dlitem"
        self.setfilename()
        # self.checkurl(self.link)

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)

        self.nlabel=QLabel(parent.ui.groupBox)
        self.nlabel.setSizePolicy(sizePolicy2)
        self.nlabel.setMaximumSize(QSize(16777215, 20))
        parent.ui.verticalLayout_3.addWidget(self.nlabel)
        self.nlabel.setText(self.filename)

        self.plabel=QLabel(parent.ui.groupBox)
        self.plabel.setSizePolicy(sizePolicy1)
        self.plabel.setMinimumSize(QSize(40, 20))
        self.plabel.setMaximumSize(QSize(40, 20))
        parent.ui.verticalLayout_4.addWidget(self.plabel)
        self.plabel.setText("0 %")     

    def updatesize(self,i):
        self.plabel.setText(str(i)+" %")

    def setfilename(self):
        temp=self.link.split("/")[-1]
        if len(temp)>100:
            temp=temp[:100]
        temp=temp.split("?")[0]
        self.filename=temp