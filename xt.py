
import sys, concurrent.futures, os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from urlextractor import *
from validations import *
from downloader import *
from dlic import *
from ui import *

widgets = None
verbose= False

import res_rc

class GUISignal(QObject):
    signal_val = Signal(int)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.pushButton.clicked.connect(lambda: Fxns.toggleMenu(self, True))
        self.ui.progressBar.setValue(0)
        self.gui_connection = GUISignal()
        # Fxns.toggleMenu(self, True)
        Fxns.fxnsdef(self)
        
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_4.clicked.connect(self.buttonClick)
        widgets.pushButton_5.clicked.connect(self.buttonClick)
        widgets.pushButton_6.clicked.connect(self.buttonClick)
        self.gui_connection.signal_val.connect(self.ui.progressBar.setValue)
        # widgets.pushButton_6.clicked.connect(self.buttonClick)
        widgets.pushButton_7.clicked.connect(self.stop)
        # widgets.pushButton_8.clicked.connect(self.buttonClick)

        self.show()

        # themeFile = "themes\deep_ocean.qss"
        # Fxns.theme(self, themeFile, True)

        widgets.stackedWidget.setCurrentWidget(widgets.page)
        widgets.pushButton_2.setStyleSheet(Fxns.selectMenu(widgets.pushButton_2.styleSheet()))
        widgets.label_2.setText("Downloads")
        # widgets.label.setText("Tasks - YTD")
        # widgets.tabWidget.setCurrentWidget(widgets.tab)
        # widgets.pushButton_7.setStyleSheet(Fxns.selectMenu(widgets.pushButton_7.styleSheet()))

        self.fails=[]
        self.skips=[]
        self.done=0
        self.total=0
        self.title="album"
        self.links=[]
        self.dlpath="downloads"
        self.alpath=os.path.join(self.dlpath,self.title)
        self.nthr=0
        self.mthr=5
        self.br=False
        self.q=[]
        self.h=[]
        self.lc=0
        # self.l=[]
        # self.c=0
        self.executor=concurrent.futures.ThreadPoolExecutor()
        self.setStatus("",False)
        self.setdefpath()
        # print(self.getdlpath())

    def setdefpath(self):
        self.dlpath=os.path.join(os.environ['USERPROFILE'],'Downloads')
        widgets.lineEdit.setText(self.dlpath)

    def getdlpath(self)->str:
        return widgets.lineEdit.text()

    def setdlpath(self):
        self.dlpath=self.getdlpath()

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "pushButton_6":
            # self.addthread()
            # addthread(self)
            inpt=self.ui.plainTextEdit.toPlainText()
            self.addurls(inpt)

        if btnName == "pushButton_2":
            widgets.stackedWidget.setCurrentWidget(widgets.page)
            Fxns.resetStyle(self, btnName)
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))
            widgets.label_2.setText("Downloads")

        if btnName == "pushButton_3":
            widgets.stackedWidget.setCurrentWidget(widgets.page_2) 
            Fxns.resetStyle(self, btnName) 
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))
            widgets.label_2.setText("Log")

        if btnName == "pushButton_5":
            selectedpath = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
            if selectedpath:
                self.dlpath=selectedpath
                widgets.lineEdit.setText(self.dlpath)

        if btnName == "pushButton_4":
            widgets.stackedWidget.setCurrentWidget(widgets.page_3)
            Fxns.resetStyle(self, btnName)
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))
            widgets.label_2.setText("About")

    def addurls(self,inpt:str)->None:
        inpt=inpt.split("\n")
        proceed=True
        validpath=True
        self.setdlpath()
        validpath=is_path_exists_or_creatable(self.dlpath)
        if validpath:
            for i in inpt:
                if not validateUrl(i):
                    self.setStatus("One or more Invalid Urls.",False)
                    proceed=False
                    break
                if i.split("/")[2]!="cyberdrop.me":
                    self.setStatus("Enter cyberdrop.me URLs only",False)
                    proceed=False
                    break
            if proceed:
                self.ui.plainTextEdit.clear()
                self.setStatus("Added",False)
                if verbose: print("added")
                for i in inpt:
                    skip=False
                    if verbose: print("Extracting")
                    self.log("Extracting")
                    self.setStatus("Extracting",True)
                    extractlinks(self,i,skip)
                    if skip:
                        if verbose: print("skipping ", i)
                        self.log("skipping "+i)
                        self.skips.append(i)
                        self.setStatus("Skipping",False)
                        continue
                    if verbose: print("Extraction Finished")
                    self.setStatus("Extraction Finished",True)
                    self.log("Extraction Finished")
                    self.log("Downloading album from "+i)
                    self.ui.label_9.setText(i)
                    self.alpath=os.path.join(self.dlpath,self.title)
                    if not os.path.exists(self.alpath):
                        os.makedirs(self.alpath)
                        
                    while self.links:
                        if self.nthr<self.mthr:
                            dl=self.links.pop(0)
                            self.q.append(Dlitem(dl[0],dl[1],self))
                            self.h.append(self.executor.submit(downld,self,self.q[-1],self.alpath))
                            if verbose: print("added")
                            self.log("Added "+str(dl))
                            self.nthr+=1
                            self.setStatus(f"Downloading Album {self.title}",True)
                    self.executor.submit(self.chkfinish)
                    self.ui.groupBox.adjustSize()
                    self.log("Finished Downloading from "+i)
                
                if verbose: print(self.done)
                if verbose: print(self.total)
                # while not self.done==self.total:
                #     self.setStatus("Downloading",True)
                # self.setStatus("Downloads Added",True)
        else:
            self.setStatus("Invalid Download Destination",False)
                
    def stop(self)->None:
        self.br=True
    
    def setStatus(self,stat:str,det:bool)->None:
        x=stat
        if det:
            if len(self.skips):
                x+=f", {len(self.skips)} URL(s) skipped"
            if len(self.fails):
                x+=f", {len(self.fails)} download(s) failed"
        self.ui.label_10.setText(str(x))
    
    def log(self,txt:str)->None:
        QListWidgetItem(txt, widgets.listWidget)
        # print(widgets.listWidget.count())
        if int(widgets.listWidget.count())>Config.LOG_BUFFER_SIZE:
            # print("del trigger")
            itemtodel=widgets.listWidget.item(0)
            widgets.listWidget.takeItem(0)
            del itemtodel

    def chkfinish(self)->None:
        while not self.done==self.total:
            self.setStatus("Downloading",True)
        self.setStatus("Downloads Finished",True)
        self.log("Finished")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("mgw.ico"))
    app.setStyle("Fusion")
    # app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = MainWindow()
    sys.exit(app.exec())