
import requests, sys, concurrent.futures,time, os, re, platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from urlextractor import *
from downloader import *
from dlic import *
from ui import *

widgets = None
verbose= True

# import res_rc

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
        # Fxns.fxnsdef(self)
        
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_4.clicked.connect(self.buttonClick)
        widgets.pushButton_5.clicked.connect(self.buttonClick)
        widgets.pushButton_6.clicked.connect(self.buttonClick)
        self.gui_connection.signal_val.connect(self.ui.progressBar.setValue)
        # widgets.pushButton_6.clicked.connect(self.buttonClick)
        # widgets.pushButton_7.clicked.connect(self.buttonClick)
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
        # self.h=[]
        # self.l=[]
        # self.c=0
        # self.br=False
        self.executor=concurrent.futures.ThreadPoolExecutor()
        self.setStatus("")
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

    def validateUrl(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, str(url))

    def addurls(self,inpt:str)->None:
        inpt=inpt.split("\n")
        proceed=True
        validpath=True
        self.setdlpath()
        validpath=is_path_exists_or_creatable(self.dlpath)
        if validpath:
            for i in inpt:
                if not self.validateUrl(i):
                    self.setStatus("One or more Invalid Urls.")
                    proceed=False
                    break
            if proceed:
                self.ui.plainTextEdit.clear()
                if verbose: print("added")
                for i in inpt:
                    skip=False
                    if verbose: print("Extracting")
                    extractlinks(self,i,skip)
                    if skip:
                        if verbose: print("skipping ", i)
                        continue
                    if verbose: print("Extraction successful")
                    self.ui.label_9.setText(i)
                    self.alpath=os.path.join(self.dlpath,self.title)
                    if not os.path.exists(self.alpath):
                        os.makedirs(self.alpath)
                    while self.links:
                        if self.nthr<self.mthr:
                            dl=self.links.pop(0)
                            self.q.append(Dlitem(dl[0],dl[1],self))
                            self.executor.submit(downld,self,self.q[-1],self.alpath)
                            if verbose: print("added")
                            self.nthr+=1
                    self.ui.groupBox.adjustSize()
        else:
            self.setStatus("Invalid Download Destination")
                
    def stop(self)->None:
        self.br=True
    
    def setStatus(self,stat)->None:
        self.ui.label_10.setText(str(stat))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    app.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(255,255,255))
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(255,255,255))
    dark_palette.setColor(QPalette.ToolTipText, QColor(255,255,255))
    dark_palette.setColor(QPalette.Text, QColor(255,255,255))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QColor(255,255,255))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(142,45,197).lighter())
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    # app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = MainWindow()
    app.setPalette(dark_palette)
    sys.exit(app.exec())