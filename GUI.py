# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.conn = sqlite3.connect('ExpertiseCar.db')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 100, 891, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 911, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(5, 1, 911, 391))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(140)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(5, 1, 911, 391))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(140)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(60, 220, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(60, 280, 57, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(60, 400, 57, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(60, 340, 57, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(60, 460, 57, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(320, 400, 57, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(320, 220, 57, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(320, 160, 71, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(320, 280, 91, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(320, 100, 81, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(320, 340, 57, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(320, 460, 57, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(590, 400, 81, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(590, 220, 57, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(590, 160, 57, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(590, 280, 57, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(590, 100, 57, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(590, 340, 81, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(590, 460, 121, 21))
        self.label_22.setObjectName("label_22")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 160, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 220, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 330, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 400, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(150, 280, 79, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 460, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(740, 460, 79, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(740, 410, 79, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_5.setGeometry(QtCore.QRect(740, 340, 79, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_6.setGeometry(QtCore.QRect(740, 280, 101, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_7.setGeometry(QtCore.QRect(440, 460, 101, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_8.setGeometry(QtCore.QRect(440, 400, 101, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_9.setGeometry(QtCore.QRect(440, 340, 101, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_10.setGeometry(QtCore.QRect(440, 280, 101, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_11.setGeometry(QtCore.QRect(440, 220, 101, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_12.setGeometry(QtCore.QRect(440, 160, 101, 22))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_13 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_13.setGeometry(QtCore.QRect(440, 100, 101, 22))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_14 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_14.setGeometry(QtCore.QRect(740, 100, 101, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_15.setGeometry(QtCore.QRect(740, 160, 101, 22))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_16 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_16.setGeometry(QtCore.QRect(740, 220, 101, 22))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.add_btn = QtWidgets.QPushButton(self.tab_4)
        self.add_btn.setGeometry(QtCore.QRect(10, 0, 80, 51))
        self.add_btn.setObjectName("add_btn")
        self.update_btn = QtWidgets.QPushButton(self.tab_4)
        self.update_btn.setGeometry(QtCore.QRect(170, 0, 80, 51))
        self.update_btn.setObjectName("update_btn")
        self.delete_btn = QtWidgets.QPushButton(self.tab_4)
        self.delete_btn.setGeometry(QtCore.QRect(820, 0, 61, 51))
        self.delete_btn.setStyleSheet("")
        self.delete_btn.setObjectName("delete_btn")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -10, 921, 141))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(0, 70, 71, 31))
        self.refresh_btn.setStyleSheet("font: 12pt \"Caladea [unknown]\";\n""")
        self.refresh_btn.setObjectName("refresh_btn")
        self.label.raise_()
        self.tabWidget.raise_()
        self.refresh_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.current_table= None
        self.add_btn.clicked.connect(self.add_data)
        self.update_btn.clicked.connect(self.update_data)
        self.delete_btn.clicked.connect(self.delete_data)
        self.refresh_btn.clicked.connect(self.refresh_data)



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Set up the tables
        self.tableWidget.setHorizontalHeaderLabels(["car_id", "car_name", "model", "fuel", "km", "age"])
        self.tableWidget_2.setHorizontalHeaderLabels(["car_id", "engine", "rights_doors", "lefts_doors", "roof", "battery_status", "lights", "airbag", "wheel", "hood", "roof_rack", "bumpers"])
        self.tableWidget_3.setHorizontalHeaderLabels(["car_id", "gearbox", "multimedia", "fog_lights", "navigation_systems"])

    def add_data(self):
        import sqlite3
    
        car_id = self.lineEdit.text()
        car_name = self.lineEdit_2.text()
        model = self.lineEdit_3.text()
        fuel = self.comboBox.currentText()
        km = self.lineEdit_4.text()
        age = self.lineEdit_5.text()
        engine = self.comboBox_2.currentText()
        rights_doors = self.comboBox_3.currentText()
        lefts_doors = self.comboBox_4.currentText()
        roof = self.comboBox_5.currentText()
        battery_status = self.comboBox_6.currentText()
        lights = self.comboBox_7.currentText()
        airbag = self.comboBox_8.currentText()
        wheel = self.comboBox_9.currentText()
        hood = self.comboBox_10.currentText()
        roof_rack = self.comboBox_11.currentText()
        bumpers = self.comboBox_12.currentText()
        gearbox = self.comboBox_13.currentText()
        multimedia = self.comboBox_14.currentText()
        fog_lights = self.comboBox_15.currentText()
        navigation_systems = self.comboBox_16.currentText()

        try:
            self.conn = sqlite3.connect('ExpertiseCar.db')
            add_query = """
            INSERT INTO Cars_info (
                car_id, car_name, model, fuel, km, age
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """
            
            self.conn.execute(
                add_query,
                (car_id, car_name, model, fuel, km, age)
            )
        
            add_query = """
            INSERT INTO Damages_info (
                car_id, engine, rights_doors, lefts_doors, roof, battery_status,
                lights, airbag, wheel, hood, roof_rack, bumpers
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            self.conn.execute(
            add_query,
            (car_id, engine, rights_doors, lefts_doors, roof, battery_status,
            lights, airbag, wheel, hood, roof_rack, bumpers)
            )

            add_query = """
            INSERT INTO Equipments (
                 car_id, gearbox, multimedia, fog_lights, navigation_systems
            )
            VALUES (?, ?, ?, ?, ?)
            """
            self.conn.execute(
            add_query,
            ( car_id, gearbox, multimedia, fog_lights, navigation_systems)
            )

            self.conn.commit()
            self.conn.close()
            self.statusbar.showMessage("Successful", 6000)
        except Exception as error:
        
            self.statusbar.showMessage("Failed ===" + str(error), 6000)

        

    def update_data(self):
        
        import sqlite3

        car_id = self.lineEdit.text()
        model = self.lineEdit_3.text()
        fuel = self.comboBox.currentText()
        km = self.lineEdit_4.text()
        age = self.lineEdit_5.text()
        engine = self.comboBox_2.currentText()
        rights_doors = self.comboBox_3.currentText()
        lefts_doors = self.comboBox_4.currentText()
        roof = self.comboBox_5.currentText()
        battery_status = self.comboBox_6.currentText()
        lights = self.comboBox_7.currentText()
        airbag = self.comboBox_8.currentText()
        wheel = self.comboBox_9.currentText()
        hood = self.comboBox_10.currentText()
        roof_rack = self.comboBox_11.currentText()
        bumpers = self.comboBox_12.currentText()
        gearbox = self.comboBox_13.currentText()
        multimedia = self.comboBox_14.currentText()
        fog_lights = self.comboBox_15.currentText()
        navigation_systems = self.comboBox_16.currentText()

        try:
            self.conn = sqlite3.connect('ExpertiseCar.db')
        
            update_query_cars_info = """
            UPDATE Cars_info
            SET model=?, fuel=?, km=?, age=?
            WHERE car_id=?
            """
            self.conn.execute(
            update_query_cars_info,
            (model, fuel, km, age, car_id)
            )

            update_query_damages_info = """
            UPDATE Damages_info
            SET engine=?, rights_doors=?, lefts_doors=?, roof=?, battery_status=?,
            lights=?, airbag=?, wheel=?, hood=?, roof_rack=?, bumpers=?
            WHERE car_id=?
            """
            self.conn.execute(
            update_query_damages_info,
            (engine, rights_doors, lefts_doors, roof, battery_status,
            lights, airbag, wheel, hood, roof_rack, bumpers, car_id)
            )

            update_query_equipments = """
            UPDATE Equipments
            SET gearbox=?, multimedia=?, fog_lights=?, navigation_systems=?
            WHERE car_id=?
            """
            self.conn.execute(
            update_query_equipments,
            (gearbox, multimedia, fog_lights, navigation_systems, car_id)
            )

            self.conn.commit()
            self.conn.close()
            self.statusbar.showMessage("Update Successful", 6000)
        except Exception as error:
            self.statusbar.showMessage("Update Failed ===" + str(error), 6000)



    def delete_data(self):

        import sqlite3

        car_id = self.lineEdit.text()

        try:
            self.conn = sqlite3.connect('ExpertiseCar.db')

            delete_query_cars_info = """
            DELETE FROM Cars_info
            WHERE car_id=?
            """
            self.conn.execute(
            delete_query_cars_info,
            (car_id,)
            )

            delete_query_damages_info = """
            DELETE FROM Damages_info
            WHERE car_id=?
            """
            self.conn.execute(
            delete_query_damages_info,
            (car_id,)
            )

            delete_query_equipments = """
            DELETE FROM Equipments
            WHERE car_id=?
            """
            self.conn.execute(
            delete_query_equipments,
            (car_id,)
            )

            self.conn.commit()
            self.conn.close()
            self.statusbar.showMessage("Deletion Successful", 6000)

        except Exception as error:
        
            self.statusbar.showMessage("Deletion Failed ===" + str(error), 6000)

    def refresh_data(self):

        import sqlite3
    
        # Clear 
        car_id = self.lineEdit.text()
        model = self.lineEdit_3.text()
        
        fuel = self.comboBox.currentText()
        km = self.lineEdit_4.text()
        age = self.lineEdit_5.text()
        engine = self.comboBox_2.currentText()
        rights_doors = self.comboBox_3.currentText()
        lefts_doors = self.comboBox_4.currentText()
        roof = self.comboBox_5.currentText()
        battery_status = self.comboBox_6.currentText()
        lights = self.comboBox_7.currentText()
        airbag = self.comboBox_8.currentText()
        wheel = self.comboBox_9.currentText()
        hood = self.comboBox_10.currentText()
        roof_rack = self.comboBox_11.currentText()
        bumpers = self.comboBox_12.currentText()
        gearbox = self.comboBox_13.currentText()
        multimedia = self.comboBox_14.currentText()
        fog_lights = self.comboBox_15.currentText()
        navigation_systems = self.comboBox_16.currentText()

        try:

            self.conn = sqlite3.connect('ExpertiseCar.db')

            
            ui.show_data_in_table("Cars_info")
            ui.show_data_in_table("Damages_info")
            ui.show_data_in_table("Equipments")

            MainWindow.show()

    
            self.statusbar.showMessage("Refreshed", 6000)

            self.conn.close()
        except Exception as error:
            self.statusbar.showMessage("Refresh failed ==="+str(error),6000)
        

        


        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "car_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "car_name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "model"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fuel"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "km"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "age"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cars_info"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "car_id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "engine"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "rights_doors"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "lefts_doors"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "roof"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "battery_status"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "lights"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "airbag"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "wheel"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "hood"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "roof_rack"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "bumpers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Damages_info"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "car_id"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "gearbox"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "multimedia"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fog_lights"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "navigation_systems"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Equipments"))
        self.label_2.setText(_translate("MainWindow", "car_id"))
        self.label_3.setText(_translate("MainWindow", "car_name"))
        self.label_4.setText(_translate("MainWindow", "model"))
        self.label_5.setText(_translate("MainWindow", "fuel"))
        self.label_6.setText(_translate("MainWindow", "age"))
        self.label_7.setText(_translate("MainWindow", "km"))
        self.label_8.setText(_translate("MainWindow", "engine"))
        self.label_9.setText(_translate("MainWindow", "airbag"))
        self.label_10.setText(_translate("MainWindow", "roof"))
        self.label_11.setText(_translate("MainWindow", "lefts_doors"))
        self.label_12.setText(_translate("MainWindow", "battery_status"))
        self.label_13.setText(_translate("MainWindow", "rights_doors"))
        self.label_14.setText(_translate("MainWindow", "ligts"))
        self.label_15.setText(_translate("MainWindow", "wheel"))
        self.label_16.setText(_translate("MainWindow", "fog_lights"))
        self.label_17.setText(_translate("MainWindow", "bumpers"))
        self.label_18.setText(_translate("MainWindow", "roof_rack"))
        self.label_19.setText(_translate("MainWindow", "gearbox"))
        self.label_20.setText(_translate("MainWindow", "hood"))
        self.label_21.setText(_translate("MainWindow", "multimedia"))
        self.label_22.setText(_translate("MainWindow", "navigation_systems"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Diesel"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Hybrid"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Gasoline"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "No"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "No"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "No"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Manual"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Automatic"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "No"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_11.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_13.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "Bad"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "Very good"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "Good"))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "Not bad"))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "Bad"))
        self.add_btn.setText(_translate("MainWindow", "ADD"))
        self.update_btn.setText(_translate("MainWindow", "UPDATE"))
        self.delete_btn.setText(_translate("MainWindow", "DELETE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Editing"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; font-style:italic;\">Expertise Form Application</span></p></body></html>"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
    
    def show_data_in_table(self, table_name):
        # Connect to the database
        conn = sqlite3.connect('ExpertiseCar.db')
        cursor = conn.cursor()

        # Fetch data from the specified table
        cursor.execute(f'SELECT * FROM {table_name}')
        data = cursor.fetchall()

        # Populate the table with data
        if table_name == "Cars_info":
            self.populate_table(self.tableWidget, data)
        elif table_name == "Damages_info":
            self.populate_table(self.tableWidget_2, data)
        elif table_name == "Equipments":
            self.populate_table(self.tableWidget_3, data)

        # Close the connection
        conn.close()

    def populate_table(self, table_widget, data):
        table_widget.setRowCount(0)

        for row_num, row_data in enumerate(data):
            table_widget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                table_widget.setItem(row_num, col_num, item)

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    import sqlite3
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.show_data_in_table("Cars_info")
    ui.show_data_in_table("Damages_info")
    ui.show_data_in_table("Equipments")

    MainWindow.show()


#connect data
    import sqlite3

    conn = sqlite3.connect('ExpertiseCar.db')

#create cursor
    cursor = conn.cursor()

#save
    conn.commit()
    
#close
    conn.close()

    

    sys.exit(app.exec_())