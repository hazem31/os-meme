from PyQt5 import QtCore, QtGui, QtWidgets
import os
import collections
import math

list_of_pro = []
list_of_hole = []

def bubble_sort_of_holes(l):
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j].loc1num > l[j+1].loc1num:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

def bubble_sort_of_holes_by_size(l):
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j].size > l[j+1].size:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp


def calibrate(x,mem_size_num):
    return (x*900)/mem_size_num

def decalibrate(x,mem_size_num):
    return math.ceil((x*mem_size_num)/900)


class process:
    def  __init__(self):
        self.name = ""
        self.num_of_seg = 0
        self.list_of_segments = []

class segment:
    def  __init__(self):
        self.name_of_seg = ""
        self.size = 0
        self.size_w = 0
        self.loc1num = 0
        self.loc2num = 0
        self.frame_of_seg = None
        self.label_of_seg = None
        self.loc1_of_seg = None
        self.loc2_of_seg = None
        self.suc = False

class hole:
    def  __init__(self):
        self.name_of_hole = ""
        self.size = 0
        self.size_w = 0
        self.loc1num = 0
        self.loc2num = 0
        self.frame_of_hole = None
        self.label_of_hole= None
        self.loc1_of_hole = None
        self.loc2_of_hole = None





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(950, 20, 231, 900))
        self.frame.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(810, 920, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 770, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.mem_size_input = QtWidgets.QLineEdit(self.centralwidget)
        self.mem_size_input.setGeometry(QtCore.QRect(350, 50, 151, 31))
        self.mem_size_input.setObjectName("mem_size_input")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.accept_mem = QtWidgets.QPushButton(self.centralwidget)
        self.accept_mem.setGeometry(QtCore.QRect(570, 50, 191, 41))
        self.accept_mem.setObjectName("accept_mem")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.process_name = QtWidgets.QLineEdit(self.centralwidget)
        self.process_name.setGeometry(QtCore.QRect(350, 210, 151, 31))
        self.process_name.setObjectName("process_name")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.num_o_seg = QtWidgets.QLineEdit(self.centralwidget)
        self.num_o_seg.setGeometry(QtCore.QRect(350, 270, 151, 31))
        self.num_o_seg.setObjectName("num_o_seg")
        self.accept_mem_2 = QtWidgets.QPushButton(self.centralwidget)
        self.accept_mem_2.setGeometry(QtCore.QRect(550, 230, 191, 41))
        self.accept_mem_2.setObjectName("accept_mem_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.seg_name = QtWidgets.QLineEdit(self.centralwidget)
        self.seg_name.setGeometry(QtCore.QRect(170, 350, 151, 31))
        self.seg_name.setObjectName("seg_name")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.seg_size = QtWidgets.QLineEdit(self.centralwidget)
        self.seg_size.setGeometry(QtCore.QRect(470, 350, 151, 31))
        self.seg_size.setObjectName("seg_size")
        self.accept_seg = QtWidgets.QPushButton(self.centralwidget)
        self.accept_seg.setGeometry(QtCore.QRect(290, 410, 191, 41))
        self.accept_seg.setObjectName("accept_seg")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.hole_start = QtWidgets.QLineEdit(self.centralwidget)
        self.hole_start.setGeometry(QtCore.QRect(220, 120, 151, 31))
        self.hole_start.setObjectName("hole_start")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(420, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.hole_size = QtWidgets.QLineEdit(self.centralwidget)
        self.hole_size.setGeometry(QtCore.QRect(570, 120, 151, 31))
        self.hole_size.setObjectName("hole_size")
        self.accept_mem_3 = QtWidgets.QPushButton(self.centralwidget)
        self.accept_mem_3.setGeometry(QtCore.QRect(550, 160, 191, 41))
        self.accept_mem_3.setObjectName("accept_mem_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 540, 256, 192))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 790, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label.hide()

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 470, 141, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 820, 141, 41))
        self.comboBox_2.setObjectName("comboBox_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mem_size_num = 0
        self.num_of_pro = 0
        self.current_seg = 0
        self.pushButton.clicked.connect(self.deallocate)
        self.accept_mem.clicked.connect(self.draw_mem)
        self.accept_mem_3.clicked.connect(self.add_hole)
        self.accept_mem_2.clicked.connect(self.add_pro)
        self.accept_seg.clicked.connect(self.add_seg1)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton.setText(_translate("MainWindow", "de-allocate"))
        self.label_6.setText(_translate("MainWindow", "memory size"))
        self.accept_mem.setText(_translate("MainWindow", "add mem size"))
        self.label_7.setText(_translate("MainWindow", "process name"))
        self.label_8.setText(_translate("MainWindow", "segs number"))
        self.accept_mem_2.setText(_translate("MainWindow", "accept process"))
        self.label_9.setText(_translate("MainWindow", "seg name"))
        self.label_10.setText(_translate("MainWindow", "seg size"))
        self.accept_seg.setText(_translate("MainWindow", "accept seg"))
        self.label_11.setText(_translate("MainWindow", "add hole start"))
        self.label_12.setText(_translate("MainWindow", "add hole size"))
        self.accept_mem_3.setText(_translate("MainWindow", "add hole"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "process list"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "error"))
        self.comboBox.setItemText(0, _translate("MainWindow", "first-fit"))
        self.comboBox.setItemText(1, _translate("MainWindow", "best-fit"))


    def add_seg(self,p1,p2,temp_seg):
        seg_temp = segment()
        seg_temp.size_w = temp_seg.size_w
        seg_temp.name_of_seg = temp_seg.name_of_seg
        seg_temp.size = p2 - p1
        seg_temp.loc1num = p1
        seg_temp.loc2num = p2
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setGeometry(QtCore.QRect(0, p1, 231, p2 - p1))
        self.frame1.setStyleSheet("background-color: rgb(0, 155, 0);")
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setObjectName("frame1")
        self.frame1.show()

        seg_temp.frame_of_seg = self.frame1

        self.label3 = QtWidgets.QLabel(self.frame1)
        self.label3.setGeometry(QtCore.QRect(0, 0, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label3.show()
        #ss = decalibrate(p2-p1,self.mem_size_num)
        #print(ss,p2-p1)
        self.label3.setText(seg_temp.name_of_seg + " " + " " + str(decalibrate(p2 - p1, self.mem_size_num)))
        self.label3.show()

        seg_temp.label_of_seg = self.label3

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        # TODO check number7
        self.label4.setGeometry(QtCore.QRect(890, p1 + 30, 55, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        # TODO check number8
        self.label5.setGeometry(QtCore.QRect(890, p2 + 5, 55, 16))
        self.label5.setObjectName("label5")
        self.label4.show()
        self.label5.show()
        self.label4.setText(str(decalibrate(p1, self.mem_size_num)))
        self.label5.setText(str(decalibrate(p2, self.mem_size_num)))

        seg_temp.loc1_of_seg = self.label4
        seg_temp.loc2_of_seg = self.label5

        list_of_pro[len(list_of_pro)-1].list_of_segments.append(seg_temp)

        self.current_seg -= 1

        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item.setText("=>>>>> " +str(seg_temp.name_of_seg) + " pelong to " +list_of_pro[len(list_of_pro)-1].name )

    def first_fit(self,tt,temp_seg):

        temp_hole = hole()

        hol = list_of_hole[tt]

        list_of_hole[tt].loc1_of_hole.setParent(None)
        list_of_hole[tt].loc2_of_hole.setParent(None)
        list_of_hole[tt].label_of_hole.setParent(None)
        list_of_hole[tt].frame_of_hole.setParent(None)

        ps = hol.loc1num
        p1 = hol.loc1num+temp_seg.size
        p2 = hol.loc2num
        p3 = hol.size_w - temp_seg.size_w
        list_of_hole.pop(tt)

        self.add_hole2(p1,p2,p3)
        self.add_seg(ps,p1,temp_seg)


    def best_fit(self,min_index,temp_seg):
        temp_hole = hole()
        tt = min_index
        hol = list_of_hole[tt]

        list_of_hole[tt].loc1_of_hole.setParent(None)
        list_of_hole[tt].loc2_of_hole.setParent(None)
        list_of_hole[tt].label_of_hole.setParent(None)
        list_of_hole[tt].frame_of_hole.setParent(None)

        ps = hol.loc1num
        p1 = hol.loc1num + temp_seg.size
        p2 = hol.loc2num
        p3 = hol.size_w - temp_seg.size_w
        list_of_hole.pop(tt)

        self.add_hole2(p1, p2 ,p3)
        self.add_seg(ps, p1, temp_seg)

    def check_and_draw(self,temp_seg):
        algo = self.comboBox.currentText()
        tt = None
        if algo == "first-fit":
            bubble_sort_of_holes(list_of_hole)
            if len(list_of_hole) > 0:
                for i in range(len(list_of_hole)):
                    if list_of_hole[i].size >= temp_seg.size:
                        tt = i
                        break

            else:
                self.label.setText("no holes")
                self.label.show()
                return

            if(tt == None):
                self.label.setText("not enough size for " + temp_seg.name_of_seg)
                self.label.show()
                return

            self.first_fit(tt,temp_seg)


        else:
            #bubble_sort_of_holes_by_size(list_of_hole)
            min1 = self.mem_size_num
            min_index = None
            if len(list_of_hole) > 0:
                for i in range(len(list_of_hole)):
                    if list_of_hole[i].size >= temp_seg.size:
                        if list_of_hole[i].size < min1:
                            min1 = list_of_hole[i].size
                            min_index = i


            else:
                self.label.setText("no holes")
                self.label.show()
                return

            if (min_index == None):
                self.label.setText("not enough size for " + temp_seg.name_of_seg)
                self.label.show()
                return

            self.best_fit(min_index, temp_seg)

        self.label.hide()
    def add_seg1(self):
        name = self.seg_name.text()
        seg_size = int(self.seg_size.text())

        temp_seg = segment()
        temp_seg.name_of_seg = name
        temp_seg.size = calibrate(seg_size,self.mem_size_num)
        #list_of_pro[-1].list_of_segments.append(temp_seg)

        if( len(list_of_pro[len(list_of_pro) - 1].list_of_segments) == list_of_pro[len(list_of_pro) - 1].num_of_seg ):
            self.label.setText("no more seg for pro")
            self.label.show()
            return


        self.check_and_draw(temp_seg)
        #self.label.hide()
    def add_pro(self):

        if(self.current_seg != 0):
            self.label.setText("finish the current process plz")
            self.label.show()
            return

        name = self.process_name.text()
        seg_num = int(self.num_o_seg.text())
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item.setText("Pname: " + str(name) + " segs num: " + str(seg_num))

        self.num_of_pro += 1
        self.current_seg = seg_num

        temp_pro = process()
        temp_pro.name = name
        temp_pro.num_of_seg = seg_num

        list_of_pro.append(temp_pro)

        self.comboBox_2.addItem(temp_pro.name)

        self.label.hide()

    def add_hole(self):
        hole_temp = hole()
        num = len(list_of_hole)
        start = int(self.hole_start.text())
        size = int(self.hole_size.text())
        hole_temp.size_w = start
        hole_temp.size = calibrate(size,self.mem_size_num)
        hole_temp.loc1num = calibrate(start,self.mem_size_num)
        hole_temp.loc2num = calibrate(start+size,self.mem_size_num)
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setGeometry(QtCore.QRect(0, hole_temp.loc1num, 231, hole_temp.size))
        self.frame1.setStyleSheet("background-color: rgb(155, 0, 0);")
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setObjectName("frame1")
        self.frame1.show()

        hole_temp.frame_of_hole = self.frame1

        self.label3 = QtWidgets.QLabel(self.frame1)
        self.label3.setGeometry(QtCore.QRect(0, 0, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label3.show()
        self.label3.setText("hole "+str(size))
        self.label3.show()


        hole_temp.label_of_hole = self.label3

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        # TODO check number5
        self.label4.setGeometry(QtCore.QRect(890, hole_temp.loc1num+30, 55, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        # TODO check number6
        self.label5.setGeometry(QtCore.QRect(890, hole_temp.loc2num+5, 55, 16))
        self.label5.setObjectName("label5")
        self.label4.show()
        self.label5.show()
        self.label4.setText(str(start))
        self.label5.setText(str(start+size))

        hole_temp.loc1_of_hole = self.label4
        hole_temp.loc2_of_hole = self.label5

        list_of_hole.append(hole_temp)


        while(not self.check()):
                c = 2

    def add_hole2(self,p1,p2,p3):
        hole_temp = hole()
        hole_temp.size_w = p3
        hole_temp.size = p2-p1
        hole_temp.loc1num = p1
        hole_temp.loc2num = p2
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setGeometry(QtCore.QRect(0, p1, 231, p2-p1))
        self.frame1.setStyleSheet("background-color: rgb(155, 0, 0);")
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setObjectName("frame1")
        self.frame1.show()

        hole_temp.frame_of_hole = self.frame1

        self.label3 = QtWidgets.QLabel(self.frame1)
        self.label3.setGeometry(QtCore.QRect(0, 0, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label3.show()
        #ss = decalibrate(p2-p1,self.mem_size_num)
        #print(ss,p2-p1)
        self.label3.setText("hole " + str(decalibrate(p2-p1,self.mem_size_num)))
        self.label3.show()

        hole_temp.label_of_hole = self.label3

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        # TODO check number3
        self.label4.setGeometry(QtCore.QRect(890, p1 + 30, 55, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        # TODO check number4
        self.label5.setGeometry(QtCore.QRect(890, p2 + 5, 55, 16))
        self.label5.setObjectName("label5")
        self.label4.show()
        self.label5.show()
        self.label4.setText(str(decalibrate(p1,self.mem_size_num)))
        self.label5.setText(str(decalibrate(p2,self.mem_size_num)))

        hole_temp.loc1_of_hole = self.label4
        hole_temp.loc2_of_hole = self.label5

        list_of_hole.append(hole_temp)



    def check(self):
        bubble_sort_of_holes(list_of_hole)
        hol = hole()
        i = 0
        while( i < len(list_of_hole)-1):
            if list_of_hole[i].loc2num == list_of_hole[i+1].loc1num:
                p1 = list_of_hole[i].loc1num
                p2 = list_of_hole[i+1].loc2num
                p3 = list_of_hole[i].size_w + list_of_hole[i+1].size_w
                list_of_hole[i + 1].loc1_of_hole.setParent(None)
                list_of_hole[i + 1].loc2_of_hole.setParent(None)
                list_of_hole[i + 1].label_of_hole.setParent(None)
                list_of_hole[i + 1].frame_of_hole.setParent(None)

                list_of_hole[i].loc1_of_hole.setParent(None)
                list_of_hole[i].loc2_of_hole.setParent(None)
                list_of_hole[i].label_of_hole.setParent(None)
                list_of_hole[i].frame_of_hole.setParent(None)

                list_of_hole.pop(i)
                list_of_hole.pop(i)

                self.add_hole2(p1, p2,p3)
                return False
            else:
                i += 1
        return True
    def draw_mem(self):
        inp_mem = 0
        if(self.mem_size_num != 0):
            self.label.setText("already added mem size")
            self.label.show()
            return

        try:
            inp_mem = int(self.mem_size_input.text())
            if(inp_mem < 900):
                self.label.setText("mem size should be >= 900")
                self.label.show()
                return
        except:
            return


        self.mem_size_num = inp_mem
        self.first_loc = QtWidgets.QLabel(self.centralwidget)
        # TODO check number2
        self.first_loc.setGeometry(QtCore.QRect(890, 20, 55, 16))
        self.first_loc.setObjectName("first_loc")
        self.last_loc = QtWidgets.QLabel(self.centralwidget)
        #TODO check number1
        self.last_loc.setGeometry(QtCore.QRect(880,900, 55, 16))
        self.last_loc.setObjectName("last_loc")
        self.last_loc.clear()
        self.last_loc.setText(str(inp_mem-1))
        self.first_loc.setText(str(0))
        self.first_loc.show()
        self.last_loc.show()
        self.label.hide()

    def draw(self):
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setGeometry(QtCore.QRect(0,300 ,231 , 70))
        self.frame1.setStyleSheet("background-color: rgb(91, 0, 0);")
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setObjectName("frame1")
        self.frame1.show()
        self.label3 = QtWidgets.QLabel(self.frame1)
        self.label3.setGeometry(QtCore.QRect(0, 0, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label3.show()
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(890, 325, 55, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(890, 370, 55, 16))
        self.label5.setObjectName("label5")
        self.label4.show()
        self.label5.show()
        self.label3.setText("P1-seg2")
        self.label4.setText("0")
        self.label5.setText("270")


    def deallocate(self):
        pro = self.comboBox_2.currentText()
        pss = None
        for i in range(len(list_of_pro)):
            if list_of_pro[i].name == pro:
                pss = i

        print(pss)
        curr = self.comboBox_2.currentIndex()
        self.comboBox_2.removeItem(curr)

        while 0 < len(list_of_pro[pss].list_of_segments):
            print(len(list_of_pro[pss].list_of_segments))

            ss = list_of_pro[pss].list_of_segments[0]

            ss.loc1_of_seg.setParent(None)
            ss.loc2_of_seg.setParent(None)
            ss.label_of_seg.setParent(None)
            ss.frame_of_seg.setParent(None)

            p1 = ss.loc1num
            p2 = ss.loc2num
            p3 = ss.size_w

            list_of_pro[pss].list_of_segments.pop(i)

            self.add_hole2(p1,p2,p3)
            while(not self.check()):
                c = 1

        list_of_pro.pop(pss)

def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys._excepthook = sys.excepthook
    sys.excepthook = exception_hook
    sys.exit(app.exec_())
