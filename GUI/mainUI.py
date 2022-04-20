
import sys
import os
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QPropertyAnimation, QRect, QParallelAnimationGroup, QEasingCurve
from PyQt5.QtGui import QIcon, QPixmap, QResizeEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow,QFrame
import _thread
from Window1 import *

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 常规操作

    def initUI(self):
        self.setGeometry(150, 150, 1380, 820)  # 设置主窗口大小和位置
        self.setWindowTitle('Icon')  # 设置主窗口的标题
        self.setWindowIcon(QIcon('web.png'))  # 设置主窗口的图标

        self.main_window = a()
        self.main_window.Window(self)
        self.main_Sidebar = QFrame(self)
        self.main_Sidebar.setGeometry(0, 0, 240, 820)  # 新增侧边栏容器

        self.main_Sidebar.setStyleSheet("background-color : green")

        self.main_Sidebar_LauncherConfig = QPushButton("启动器设置",self.main_Sidebar)
        self.main_Sidebar_LauncherConfig.setGeometry(0, 200, 240, 100)
        self.show()  # 显示主窗口

    def mainUI_Resize(self,w,h):
        self.main_Sidebar.setGeometry(0 * (w / 1380), 0 * (h / 820), 240 * (w / 1380), 820 * (h / 820))
        self.main_Sidebar_LauncherConfig.setGeometry(0 * (w / 1380), 200 * (h / 820), 240 * (w / 1380), 100 * (h / 820))
    def mainUI_Sidebar_Hide_1(self):
        self.main_Sidebar.hide()
    def resizeEvent(self,e):
        QWidget.resizeEvent(self, e)
        w = e.size().width()
        h = e.size().height()
        self.mainUI_Resize(w,h)
        self.main_window.Window1_Resize(w,h)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Launcher()

    sys.exit(app.exec_())
