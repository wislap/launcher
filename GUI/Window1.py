# coding=gbk
from mainUI import *
import sys
import os
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget
import _thread
from qss import *
import time

class a:

    def Window(self, window):
        self.button_Launch = QPushButton("������Ϸ", window)
        self.button_Launch.setGeometry(1020, 640, 250, 90)  # ������Ϸ��ť
        self.button_Launch.setStyleSheet(button_qss_1)
        self.button_Launch.clicked.connect(self.Launch_asyncio)  # ��������Ϸ��ť�󶨵�launch��

        self.button_LaunchSetup = QPushButton("��������", window)
        self.button_LaunchSetup.setGeometry(1020, 560, 250, 65)
        self.button_LaunchSetup.setStyleSheet(button_qss_1)
        self.button_LaunchSetup.clicked.connect(self.LaunchSetup)

        Launcher.mainUI_Sidebar_Hide_1(Launcher.initUI)
    def LaunchSetup(self):

       self.button_Launch.hide()
       self.button_LaunchSetup.hide()


    def Launch_asyncio(self):
        _thread.start_new_thread(thead_open, ())

    def Window1_Resize(self,w,h):
        self.button_Launch.setGeometry(1020 * (w / 1380), 640 * (h / 820), 250 * (w / 1380), 90 * (h / 820))
        self.button_LaunchSetup.setGeometry(1020 * (w / 1380), 560 * (h / 820), 250 * (w / 1380),65 * (h / 820))



def thead_open():
    JavaPath = r"F:\jre\jre"  # JAVA��·��
    mcJVM = r'''java -Dminecraft.client.jar=.minecraft\versions\1.16.5\1.16.5.jar -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=16M -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -Xmn128m -Xmx6000m -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path=F:\mc\ԭ��mc\.minecraft\versions\1.16.5\natives -Dminecraft.launcher.brand=HMCL -Dminecraft.launcher.version=3.3.188 -cp F:\mc\ԭ��mc\.minecraft\libraries\com\mojang\patchy\1.3.9\patchy-1.3.9.jar;F:\mc\ԭ��mc\.minecraft\libraries\oshi-project\oshi-core\1.1\oshi-core-1.1.jar;F:\mc\ԭ��mc\.minecraft\libraries\net\java\dev\jna\jna\4.4.0\jna-4.4.0.jar;F:\mc\ԭ��mc\.minecraft\libraries\net\java\dev\jna\platform\3.4.0\platform-3.4.0.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\ibm\icu\icu4j\66.1\icu4j-66.1.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\mojang\javabridge\1.0.22\javabridge-1.0.22.jar;F:\mc\ԭ��mc\.minecraft\libraries\net\sf\jopt-simple\jopt-simple\5.0.3\jopt-simple-5.0.3.jar;F:\mc\ԭ��mc\.minecraft\libraries\io\netty\netty-all\4.1.25.Final\netty-all-4.1.25.Final.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\google\guava\guava\21.0\guava-21.0.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\apache\commons\commons-lang3\3.5\commons-lang3-3.5.jar;F:\mc\ԭ��mc\.minecraft\libraries\commons-io\commons-io\2.5\commons-io-2.5.jar;F:\mc\ԭ��mc\.minecraft\libraries\commons-codec\commons-codec\1.10\commons-codec-1.10.jar;F:\mc\ԭ��mc\.minecraft\libraries\net\java\jinput\jinput\2.0.5\jinput-2.0.5.jar;F:\mc\ԭ��mc\.minecraft\libraries\net\java\jutils\jutils\1.0.0\jutils-1.0.0.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\mojang\brigadier\1.0.17\brigadier-1.0.17.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\mojang\datafixerupper\4.0.26\datafixerupper-4.0.26.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\google\code\gson\gson\2.8.0\gson-2.8.0.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\mojang\authlib\2.1.28\authlib-2.1.28.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\apache\commons\commons-compress\1.8.1\commons-compress-1.8.1.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\apache\httpcomponents\httpclient\4.3.3\httpclient-4.3.3.jar;F:\mc\ԭ��mc\.minecraft\libraries\commons-logging\commons-logging\1.1.3\commons-logging-1.1.3.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\apache\httpcomponents\httpcore\4.3.2\httpcore-4.3.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\it\unimi\dsi\fastutil\8.2.1\fastutil-8.2.1.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\apache\logging\log4j\log4j-api\2.8.1\log4j-api-2.8.1.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\apache\logging\log4j\log4j-core\2.8.1\log4j-core-2.8.1.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl\3.2.2\lwjgl-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl-jemalloc\3.2.2\lwjgl-jemalloc-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl-openal\3.2.2\lwjgl-openal-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl-opengl\3.2.2\lwjgl-opengl-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl-glfw\3.2.2\lwjgl-glfw-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl-stb\3.2.2\lwjgl-stb-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\org\lwjgl\lwjgl-tinyfd\3.2.2\lwjgl-tinyfd-3.2.2.jar;F:\mc\ԭ��mc\.minecraft\libraries\com\mojang\text2speech\1.11.3\text2speech-1.11.3.jar;F:\mc\ԭ��mc\.minecraft\versions\1.16.5\1.16.5.jar net.minecraft.client.main.Main --username 12345 --version "HMCL 3.3.188" --gameDir F:\mc\ԭ��mc\.minecraft --assetsDir F:\mc\ԭ��mc\.minecraft\assets --assetIndex 1.16 --uuid 704c82d6e63f3dceb5a9116eeff85494 --accessToken d494343b366a479fb4ce2a174ee0f69b --userType mojang --versionType "HMCL 3.3.188" --width 854 --height 480'''
    os.system(JavaPath)  # �л���java���ڵ�·��
    os.system(mcJVM)  # ��jvm����������mc
