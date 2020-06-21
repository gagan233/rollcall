# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AMSgrid.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.MainTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.loginNameEdit = QtWidgets.QLineEdit(self.MainTab)
        self.loginNameEdit.setObjectName("loginNameEdit")
        self.gridLayout_4.addWidget(self.loginNameEdit, 0, 3, 1, 2)
        self.faceButton = QtWidgets.QPushButton(self.MainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faceButton.sizePolicy().hasHeightForWidth())
        self.faceButton.setSizePolicy(sizePolicy)
        self.faceButton.setMinimumSize(QtCore.QSize(0, 100))
        self.faceButton.setObjectName("faceButton")
        self.gridLayout_4.addWidget(self.faceButton, 2, 1, 3, 4)
        self.loginPAsswordEdit = QtWidgets.QLineEdit(self.MainTab)
        self.loginPAsswordEdit.setText("")
        self.loginPAsswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPAsswordEdit.setReadOnly(False)
        self.loginPAsswordEdit.setObjectName("loginPAsswordEdit")
        self.gridLayout_4.addWidget(self.loginPAsswordEdit, 1, 3, 1, 2)
        self.loginButton = QtWidgets.QPushButton(self.MainTab)
        self.loginButton.setObjectName("loginButton")
        self.gridLayout_4.addWidget(self.loginButton, 1, 5, 1, 1)
        self.registerButton = QtWidgets.QPushButton(self.MainTab)
        self.registerButton.setObjectName("registerButton")
        self.gridLayout_4.addWidget(self.registerButton, 0, 5, 1, 1)
        self.logoutButton = QtWidgets.QPushButton(self.MainTab)
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout_4.addWidget(self.logoutButton, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.MainTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.MainTab, "")
        self.StudentTab = QtWidgets.QWidget()
        self.StudentTab.setObjectName("StudentTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.StudentTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.StudentTab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.encodeButton = QtWidgets.QPushButton(self.StudentTab)
        self.encodeButton.setObjectName("encodeButton")
        self.verticalLayout_3.addWidget(self.encodeButton)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imageLabel = QtWidgets.QLabel(self.StudentTab)
        self.imageLabel.setMinimumSize(QtCore.QSize(320, 0))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_2.addWidget(self.imageLabel)
        self.openCameraButton = QtWidgets.QPushButton(self.StudentTab)
        self.openCameraButton.setObjectName("openCameraButton")
        self.verticalLayout_2.addWidget(self.openCameraButton)
        self.takePhotoButton = QtWidgets.QPushButton(self.StudentTab)
        self.takePhotoButton.setObjectName("takePhotoButton")
        self.verticalLayout_2.addWidget(self.takePhotoButton)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 4, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deleteRecordButton = QtWidgets.QPushButton(self.StudentTab)
        self.deleteRecordButton.setObjectName("deleteRecordButton")
        self.gridLayout_2.addWidget(self.deleteRecordButton, 1, 1, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.StudentTab)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 0, 1, 1, 1)
        self.updateRecordButton = QtWidgets.QPushButton(self.StudentTab)
        self.updateRecordButton.setObjectName("updateRecordButton")
        self.gridLayout_2.addWidget(self.updateRecordButton, 1, 0, 1, 1)
        self.addRecordButton = QtWidgets.QPushButton(self.StudentTab)
        self.addRecordButton.setObjectName("addRecordButton")
        self.gridLayout_2.addWidget(self.addRecordButton, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.student_name = QtWidgets.QLabel(self.StudentTab)
        self.student_name.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.student_name.setObjectName("student_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.student_name)
        self.student_name_3 = QtWidgets.QLabel(self.StudentTab)
        self.student_name_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.student_name_3.setObjectName("student_name_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.student_name_3)
        self.label = QtWidgets.QLabel(self.StudentTab)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.student_name_2 = QtWidgets.QLabel(self.StudentTab)
        self.student_name_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.student_name_2.setObjectName("student_name_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.student_name_2)
        self.branchEdit = QtWidgets.QLineEdit(self.StudentTab)
        self.branchEdit.setObjectName("branchEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.branchEdit)
        self.genderEdit = QtWidgets.QLineEdit(self.StudentTab)
        self.genderEdit.setObjectName("genderEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.genderEdit)
        self.roll_noEdit = QtWidgets.QLineEdit(self.StudentTab)
        self.roll_noEdit.setObjectName("roll_noEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roll_noEdit)
        self.stu_nameEdit = QtWidgets.QLineEdit(self.StudentTab)
        self.stu_nameEdit.setObjectName("stu_nameEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stu_nameEdit)
        self.semesterEdit = QtWidgets.QLineEdit(self.StudentTab)
        self.semesterEdit.setObjectName("semesterEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.semesterEdit)
        self.student_name_4 = QtWidgets.QLabel(self.StudentTab)
        self.student_name_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.student_name_4.setObjectName("student_name_4")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.student_name_4)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.StudentTab, "")
        self.ViewDBTab = QtWidgets.QWidget()
        self.ViewDBTab.setObjectName("ViewDBTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ViewDBTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.ViewDBTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.rollStuEdit = QtWidgets.QLineEdit(self.ViewDBTab)
        self.rollStuEdit.setObjectName("rollStuEdit")
        self.horizontalLayout_2.addWidget(self.rollStuEdit)
        self.searchStuButton = QtWidgets.QPushButton(self.ViewDBTab)
        self.searchStuButton.setObjectName("searchStuButton")
        self.horizontalLayout_2.addWidget(self.searchStuButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.stutableWidget = QtWidgets.QTableWidget(self.ViewDBTab)
        self.stutableWidget.setObjectName("stutableWidget")
        self.stutableWidget.setColumnCount(0)
        self.stutableWidget.setRowCount(0)
        self.verticalLayout_5.addWidget(self.stutableWidget)
        self.refreshStuButton = QtWidgets.QPushButton(self.ViewDBTab)
        self.refreshStuButton.setObjectName("refreshStuButton")
        self.verticalLayout_5.addWidget(self.refreshStuButton)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.ViewDBTab, "")
        self.ReportTab = QtWidgets.QWidget()
        self.ReportTab.setObjectName("ReportTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.ReportTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.ReportTab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.rollAEdit = QtWidgets.QLineEdit(self.ReportTab)
        self.rollAEdit.setObjectName("rollAEdit")
        self.horizontalLayout_3.addWidget(self.rollAEdit)
        self.searchrollAButton = QtWidgets.QPushButton(self.ReportTab)
        self.searchrollAButton.setObjectName("searchrollAButton")
        self.horizontalLayout_3.addWidget(self.searchrollAButton)
        self.label_4 = QtWidgets.QLabel(self.ReportTab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.branchAEdit = QtWidgets.QLineEdit(self.ReportTab)
        self.branchAEdit.setObjectName("branchAEdit")
        self.horizontalLayout_3.addWidget(self.branchAEdit)
        self.searchAButton = QtWidgets.QPushButton(self.ReportTab)
        self.searchAButton.setObjectName("searchAButton")
        self.horizontalLayout_3.addWidget(self.searchAButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.atentableWidget = QtWidgets.QTableWidget(self.ReportTab)
        self.atentableWidget.setObjectName("atentableWidget")
        self.atentableWidget.setColumnCount(0)
        self.atentableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.atentableWidget)
        self.refreshAButton = QtWidgets.QPushButton(self.ReportTab)
        self.refreshAButton.setObjectName("refreshAButton")
        self.verticalLayout_4.addWidget(self.refreshAButton)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.ReportTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.faceButton.setText(_translate("MainWindow", "Start Face Recognition"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.logoutButton.setText(_translate("MainWindow", "Logout"))
        self.label_5.setText(_translate("MainWindow", "Login!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), _translate("MainWindow", "Face Recognition"))
        self.encodeButton.setText(_translate("MainWindow", "Retrain Model"))
        self.imageLabel.setText(_translate("MainWindow", "Camera will be displayed here."))
        self.openCameraButton.setText(_translate("MainWindow", "Open Camera"))
        self.takePhotoButton.setText(_translate("MainWindow", "Take photograph"))
        self.deleteRecordButton.setText(_translate("MainWindow", "Delete Record"))
        self.clearButton.setText(_translate("MainWindow", "Clear All Fields"))
        self.updateRecordButton.setText(_translate("MainWindow", "Update Record"))
        self.addRecordButton.setText(_translate("MainWindow", "Add Record"))
        self.student_name.setText(_translate("MainWindow", "Student Name"))
        self.student_name_3.setText(_translate("MainWindow", "Roll No"))
        self.label.setText(_translate("MainWindow", "Gender"))
        self.student_name_2.setText(_translate("MainWindow", "Branch"))
        self.student_name_4.setText(_translate("MainWindow", "Semester"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StudentTab), _translate("MainWindow", "Student Database"))
        self.label_2.setText(_translate("MainWindow", "Enter Roll No"))
        self.searchStuButton.setText(_translate("MainWindow", "Search"))
        self.refreshStuButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ViewDBTab), _translate("MainWindow", "View Student Database"))
        self.label_3.setText(_translate("MainWindow", "Enter Roll No"))
        self.searchrollAButton.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Enter Branch"))
        self.searchAButton.setText(_translate("MainWindow", "Search"))
        self.refreshAButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ReportTab), _translate("MainWindow", "Attendance Report"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
