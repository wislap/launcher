import sys
import os
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
import _thread

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 常规操作

    global JavaPath
    global mcJVM
    JavaPath = r"C:\Program Files\Java\jdk1.8.0_161\bin"  # JAVA的路径
    mcJVM = r'''
     java -Dminecraft.client.jar=.minecraft\versions\1.16.5\1.16.5.jar -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=16M -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -Xmn128m -Xmx6000m -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path=F:\mc\原版mc\.minecraft\versions\1.16.5\natives -Dminecraft.launcher.brand=HMCL -Dminecraft.launcher.version=3.3.188 -cp F:\mc\原版mc\.minecraft\libraries\com\mojang\patchy\1.3.9\patchy-1.3.9.jar;F:\mc\原版mc\.minecraft\libraries\oshi-project\oshi-core\1.1\oshi-core-1.1.jar;F:\mc\原版mc\.minecraft\libraries\net\java\dev\jna\jna\4.4.0\jna-4.4.0.jar;F:\mc\原版mc\.minecraft\libraries\net\java\dev\jna\platform\3.4.0\platform-3.4.0.jar;F:\mc\原版mc\.minecraft\libraries\com\ibm\icu\icu4j\66.1\icu4j-66.1.jar;F:\mc\原版mc\.minecraft\libraries\com\mojang\javabridge\1.0.22\javabridge-1.0.22.jar;F:\mc\原版mc\.minecraft\libraries\net\sf\jopt-simple\jopt-simple\5.0.3\jopt-simple-5.0.3.jar;F:\mc\原版mc\.minecraft\libraries\io\netty\netty-all\4.1.25.Final\netty-all-4.1.25.Final.jar;F:\mc\原版mc\.minecraft\libraries\com\google\guava\guava\21.0\guava-21.0.jar;F:\mc\原版mc\.minecraft\libraries\org\apache\commons\commons-lang3\3.5\commons-lang3-3.5.jar;F:\mc\原版mc\.minecraft\libraries\commons-io\commons-io\2.5\commons-io-2.5.jar;F:\mc\原版mc\.minecraft\libraries\commons-codec\commons-codec\1.10\commons-codec-1.10.jar;F:\mc\原版mc\.minecraft\libraries\net\java\jinput\jinput\2.0.5\jinput-2.0.5.jar;F:\mc\原版mc\.minecraft\libraries\net\java\jutils\jutils\1.0.0\jutils-1.0.0.jar;F:\mc\原版mc\.minecraft\libraries\com\mojang\brigadier\1.0.17\brigadier-1.0.17.jar;F:\mc\原版mc\.minecraft\libraries\com\mojang\datafixerupper\4.0.26\datafixerupper-4.0.26.jar;F:\mc\原版mc\.minecraft\libraries\com\google\code\gson\gson\2.8.0\gson-2.8.0.jar;F:\mc\原版mc\.minecraft\libraries\com\mojang\authlib\2.1.28\authlib-2.1.28.jar;F:\mc\原版mc\.minecraft\libraries\org\apache\commons\commons-compress\1.8.1\commons-compress-1.8.1.jar;F:\mc\原版mc\.minecraft\libraries\org\apache\httpcomponents\httpclient\4.3.3\httpclient-4.3.3.jar;F:\mc\原版mc\.minecraft\libraries\commons-logging\commons-logging\1.1.3\commons-logging-1.1.3.jar;F:\mc\原版mc\.minecraft\libraries\org\apache\httpcomponents\httpcore\4.3.2\httpcore-4.3.2.jar;F:\mc\原版mc\.minecraft\libraries\it\unimi\dsi\fastutil\8.2.1\fastutil-8.2.1.jar;F:\mc\原版mc\.minecraft\libraries\org\apache\logging\log4j\log4j-api\2.8.1\log4j-api-2.8.1.jar;F:\mc\原版mc\.minecraft\libraries\org\apache\logging\log4j\log4j-core\2.8.1\log4j-core-2.8.1.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl\3.2.2\lwjgl-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl-jemalloc\3.2.2\lwjgl-jemalloc-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl-openal\3.2.2\lwjgl-openal-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl-opengl\3.2.2\lwjgl-opengl-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl-glfw\3.2.2\lwjgl-glfw-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl-stb\3.2.2\lwjgl-stb-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\org\lwjgl\lwjgl-tinyfd\3.2.2\lwjgl-tinyfd-3.2.2.jar;F:\mc\原版mc\.minecraft\libraries\com\mojang\text2speech\1.11.3\text2speech-1.11.3.jar;F:\mc\原版mc\.minecraft\versions\1.16.5\1.16.5.jar net.minecraft.client.main.Main --username 12345 --version "HMCL 3.3.188" --gameDir F:\mc\原版mc\.minecraft --assetsDir F:\mc\原版mc\.minecraft\assets --assetIndex 1.16 --uuid 704c82d6e63f3dceb5a9116eeff85494 --accessToken d494343b366a479fb4ce2a174ee0f69b --userType mojang --versionType "HMCL 3.3.188" --width 854 --height 480
        '''  # 启动游戏的jvm参数
    def initUI(self):
        global button_Launch
        button_Launch = QPushButton("启动游戏", self)
        button_Launch.setGeometry(150, 150, 100, 100)  # 启动游戏按钮

        button_Launch.clicked.connect(self.Launch)  # 将启动游戏按钮绑定到launch槽

        button_LaunchSetup = QPushButton("启动设置", self)
        button_LaunchSetup.setGeometry(150, 250, 100, 100)

        button_LaunchSetup.clicked.connect(self.LaunchSetup)

        button_Launch.setStyleSheet(
        '''
        QPushButton { 
            color: rgb(200, 20, 50) ;
            border-radius: 2em;  
        }
        '''
        )

        self.setGeometry(150, 150, 1380, 820)  # 设置主窗口大小和位置
        self.setWindowTitle('Icon')  # 设置主窗口的标题
        self.setWindowIcon(QIcon('web.png'))  # 设置主窗口的图标
        self.show()  # 显示主窗口

    def LaunchSetup(self):
        button_Launch.hide()

    def Launch(self):
        _thread.start_new_thread(thead_open,())
        #os.system("cd" + JavaPath)  # 切换到java所在的路径
        #os.system(mcJVM)  # 用jvm参数来启动mc

def thead_open():
    os.system("cd" + JavaPath)  # 切换到java所在的路径
    os.system(mcJVM)  # 用jvm参数来启动mc


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Launcher()

    sys.exit(app.exec_())


