from xt import *

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class Fxns(MainWindow):
    # def maximize_restore(self):
    #     global GLOBAL_STATE
    #     status = GLOBAL_STATE
    #     if status == False:
    #         self.showMaximized()
    #         GLOBAL_STATE = True
    #         # self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
    #         self.ui.pushButton_2.setToolTip("Restore")
    #         self.ui.pushButton_2.setIcon(QIcon(u":/icons/icons/icon_restore.png"))
    #     else:
    #         GLOBAL_STATE = False
    #         self.showNormal()
    #         self.resize(self.width()+1, self.height()+1)
    #         # self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
    #         self.ui.pushButton_2.setToolTip("Maximize")
    #         self.ui.pushButton_2.setIcon(QIcon(u":/icons/icons/icon_maximize.png"))

    def returStatus(self):
        return GLOBAL_STATE

    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def toggleMenu(self, enable):
        if enable:
            width = self.ui.frame.width()
            maxExtend = Config.MENU_WIDTH
            standard = 50

            if width == 50:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.frame, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def selectMenu(getStyle):
        select = getStyle + Config.MENU_SELECTED_STYLESHEET
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace(Config.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.frame.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(Fxns.selectMenu(w.styleSheet()))

    def resetStyle(self, widget, all=False):
        for w in self.ui.frame.findChildren(QPushButton):
            if not all:
                if w.objectName() != widget:
                    w.setStyleSheet(Fxns.deselectMenu(w.styleSheet()))
                    # print("reset except one")
            else:
                w.setStyleSheet(Fxns.deselectMenu(w.styleSheet()))
                # print("reset all")
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.centralwidget.setStyleSheet(str)

    def fxnsdef(self):
        # pass
        # def dobleClickMaximizeRestore(event):
        #     if event.type() == QEvent.MouseButtonDblClick:
        #         QTimer.singleShot(250, lambda: Fxns.maximize_restore(self))
        # self.ui.frame_3.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # if Config.ENABLE_CUSTOM_TITLE_BAR:
        #     self.setWindowFlags(Qt.FramelessWindowHint)
        #     self.setAttribute(Qt.WA_TranslucentBackground)

            # def moveWindow(event):
            #     if Fxns.returStatus(self):
            #         Fxns.maximize_restore(self)
            #     if event.buttons() == Qt.LeftButton:
            #         self.move(self.pos() + event.globalPos() - self.dragPos)
            #         self.dragPos = event.globalPos()
            #         event.accept()
            # self.ui.frame_3.mouseMoveEvent = moveWindow

        # DROP SHADOW
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(17)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 0, 0, 150))
        # self.ui.frame_12.setGraphicsEffect(self.shadow)

        # self.sizegrip = QSizeGrip(self.ui.frame_rs)
        # self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # self.ui.pushButton_3.clicked.connect(lambda: self.showMinimized())
        # self.ui.pushButton_2.clicked.connect(lambda: Fxns.maximize_restore(self))
        # self.ui.pushButton.clicked.connect(lambda: self.close())
        self.setMinimumSize(850,510)
        self.setMaximumSize(850,510)