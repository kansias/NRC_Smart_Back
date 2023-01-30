# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtSerialPort
import serial
# import numpy as np
import os

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())
    
    
class Ui_MainWindow(object):
    available_port = QtSerialPort.QSerialPortInfo().availablePorts()
    
    portName = ""
    label_list = []
    for x in available_port:
        portName = x.portName()
    # print(portName)
    
    arduino = ""
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1192, 600)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(120)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_home_stack_2 = QFrame(self.verticalFrame)
        self.frame_home_stack_2.setObjectName(u"frame_home_stack_2")
        self.frame_home_stack_2.setMaximumSize(QSize(16777215, 80))
        self.frame_home_stack_2.setStyleSheet(u"background-color : rgb(180, 220, 255);\n"
"")
        self.frame_home_stack_2.setFrameShadow(QFrame.Plain)
        self.frame_home_stack = QHBoxLayout(self.frame_home_stack_2)
        self.frame_home_stack.setSpacing(0)
        self.frame_home_stack.setObjectName(u"frame_home_stack")
        self.frame_home_stack.setContentsMargins(0, 0, 0, 0)
        self.frame_serial = QFrame(self.frame_home_stack_2)
        self.frame_serial.setObjectName(u"frame_serial")
        self.frame_serial.setMaximumSize(QSize(16777215, 80))
        self.frame_serial.setStyleSheet(u"border : none;")
        self.frame_serial.setFrameShape(QFrame.StyledPanel)
        self.frame_serial.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_serial)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_serial = QLineEdit(self.frame_serial)
        self.lineEdit_serial.setObjectName(u"lineEdit_serial")
        self.lineEdit_serial.setMinimumSize(QSize(250, 0))
        self.lineEdit_serial.setAlignment(Qt.AlignCenter)
        self.lineEdit_serial.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_serial)

        self.button_connet = QPushButton(self.frame_serial)
        self.button_connet.setObjectName(u"button_connet")
        self.button_connet.setEnabled(False)
        self.button_connet.setStyleSheet(u"QPushButton {\n"
"  display: inline-block;\n"
"  padding: 10px 15px;\n"
"  font-size: 15px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: rgb(243, 169, 11);\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  box-shadow: 0 9px #999;\n"
"  font-weight : 900;\n"
"}\n"
"/*\n"
"QPushButton:hover {\n"
"	background-color: #3e8e41;\n"
"}*/\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #306f32;\n"
"}")

        self.horizontalLayout_2.addWidget(self.button_connet)


        self.frame_home_stack.addWidget(self.frame_serial, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_start = QFrame(self.frame_home_stack_2)
        self.frame_start.setObjectName(u"frame_start")
        self.frame_start.setMaximumSize(QSize(16777215, 80))
        self.frame_start.setStyleSheet(u"border :none;")
        self.frame_start.setFrameShape(QFrame.StyledPanel)
        self.frame_start.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_start)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_start = QPushButton(self.frame_start)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setMinimumSize(QSize(250, 35))
        self.button_start.setMaximumSize(QSize(16777215, 35))
        self.button_start.setStyleSheet(u"QPushButton {\n"
"  display: inline-block;\n"
"  font: 12pt;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #000000;\n"
"  background-color: #eeeeee;\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  font-weight : 900;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"	\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(100,100,100,200);\n"
"    font-weight : 60;\n"
"}")

        self.horizontalLayout.addWidget(self.button_start)


        self.frame_home_stack.addWidget(self.frame_start, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_home_stack_2, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.verticalFrame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        
        # 10 x 6 grid label 생성
        for i in range(10):
            for j in range(6):
                Ui_MainWindow.label_list.append(QLabel(self.centralwidget))
                Ui_MainWindow.label_list[i*6+j].setObjectName(u"label_"+str(i*6+j))
                sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(Ui_MainWindow.label_list[i*6+j].sizePolicy().hasHeightForWidth())
                Ui_MainWindow.label_list[i*6+j].setMinimumSize(QSize(50, 50))
                Ui_MainWindow.label_list[i*6+j].setMaximumSize(QSize(50, 50))
                # sizepolicy Maximum
                Ui_MainWindow.label_list[i*6+j].setSizePolicy(sizePolicy1)
                # set label icon , path = ./icon/circle.png
                Ui_MainWindow.label_list[i*6+j].setTextFormat(Qt.MarkdownText)
                Ui_MainWindow.label_list[i*6+j].setPixmap(QPixmap(u"./icon/circle.png"))
                # 이미지 크기에 맞게 라벨 크기 조절
                Ui_MainWindow.label_list[i*6+j].setScaledContents(True)

                Ui_MainWindow.label_list[i*6+j].setWordWrap(False)
                Ui_MainWindow.label_list[i*6+j].setOpenExternalLinks(False)
                self.gridLayout.addWidget(Ui_MainWindow.label_list[i*6+j], i, j) # 라벨 생성 및 배치 초기위치 : (0,0) 마지막 위치: (9,5)


        # 그리드 간격을 동일하게 설정
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setContentsMargins(10, 10, 10, 10) #



        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_serial.setText(QCoreApplication.translate("MainWindow", u"연결된 장치가 없습니다.", None))
        self.button_connet.setText(QCoreApplication.translate("MainWindow", u"장치를 연결 후 재실행 해주세요", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        # all label text = ""
        for i in range(60):
            Ui_MainWindow.label_list[i].setText(QCoreApplication.translate("MainWindow", u"", None))
            
        if Ui_MainWindow.portName == "":    
            self.lineEdit_serial.setText(QCoreApplication.translate("MainWindow", u"연결된 장치가 없습니다", None))
            self.button_connet.setText(QCoreApplication.translate("MainWindow", u"장치를 연결 후 재실행 해주세요", None))
        else:
            Thread_data_log.main.arduino = serial.Serial( Ui_MainWindow.portName , 57600)
            self.lineEdit_serial.setText(QCoreApplication.translate("MainWindow", Ui_MainWindow.portName, None))
            self.button_connet.setText(QCoreApplication.translate("MainWindow", u"장치 연결 됨", None))
            self.button_connet.setStyleSheet(u"QPushButton {\n"
        "  display: inline-block;\n"
        "  padding: 10px 15px;\n"
        "  font-size: 15px;\n"
        "  cursor: pointer;\n"
        "  text-align: center;\n"
        "  text-decoration: none;\n"
        "  outline: none;\n"
        "  color: #fff;\n"
        "  background-color: rgb(76, 175, 80);\n"
        "  border: none;\n"
        "  border-radius: 15px;\n"
        "  box-shadow: 0 9px #999;\n"
        "  font-weight : 900;\n"
        "}\n"
        "/*\n"
        "QPushButton:hover {\n"
        "	background-color: #3e8e41;\n"
        "}*/\n"
        "\n"
        "QPushButton:pressed {\n"
        "  background-color: #306f32;\n"
        "}")
                # self.label.setText("")

    # retranslateUi

class Thread_data_log(QThread):
    main = Ui_MainWindow()
    
    button_data = Signal(list)
    def __init__(self):
            super(Thread_data_log, self).__init__()
            self.work = True
    def run(self):
        # if Thread_data_log.main.arduino.isOpen():
        #     pass
        # else:
            # Thread_data_log.main.arduino = serial.Serial( Ui_MainWindow.portName , 57600)
        #     self.usleep(500)
        while self.work:
            try:
                Thread_data_log.main.arduino.flushInput()
                Thread_data_log.main.arduino.flushOutput()
                if Thread_data_log.main.arduino.readable():
                    data = Thread_data_log.main.arduino.readline()
                    data = data.decode()[: len(data) - 2]
                    data = data.split(",")
                    data = list(map(str, data))
                    if len(data) == 60:
                        self.button_data.emit(data)
                        self.usleep(2) # usermode ref = 100ms   
                        # print(data)
                    # Thread_data_log.main.arduino.flush()
            except Exception as ex:
                #print(ex)
                pass
    def stop(self):
        self.work = False
        # Thread_data_log.main.arduino.flush()
        Thread_data_log.main.arduino.reset_input_buffer()
        Thread_data_log.main.arduino.reset_output_buffer()
        # if Thread_data_log.main.arduino.isOpen():
        #     Thread_data_log.main.arduino.close()
        #     self.usleep(5)
        self.quit()
        
        
class Window(QMainWindow):
    log_data_thread = Thread_data_log()
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.button_start.clicked.connect(self.clicked_start)
        self.log_data_thread.button_data.connect(self.show_button)
        
    def clicked_start(self):
        self.log_data_thread.start()
        self.log_data_thread.work = True
        # label icon init
        for i in range(60):
            Ui_MainWindow.label_list[i].setPixmap(QPixmap(u"./icon/circle.png"))
        self.ui.button_start.setEnabled(False)
        self.ui.button_start.setText("STARTING")
        
        # print(Window.log_data_thread.button_data)
        
    def show_button(self, data):
        print(data)
        for i in range(len(self.ui.label_list)):
            if data[i] == 1:
                Ui_MainWindow.label_list[i].setPixmap(QPixmap(u"./icon/circle.png"))
            elif data[i] == 0:
                Ui_MainWindow.label_list[i].setPixmap(QPixmap(u"./icon/lens.png"))
            else:
                Ui_MainWindow.label_list[i].setPixmap(QPixmap(u"./icon/circle.png"))
        
if __name__ == "__main__":
    import sys
    # SHOW gui window
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec_())