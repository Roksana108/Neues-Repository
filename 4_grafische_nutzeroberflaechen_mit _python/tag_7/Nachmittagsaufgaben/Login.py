# Form implementation generated from reading ui file 'aufhabe_3.15.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 80, 311, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_name)
        self.label_email = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_email)
        self.label_password = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_password)
        self.label_passwort_wdh = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_passwort_wdh.setObjectName("label_passwort_wdh")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_passwort_wdh)
        self.button_ok = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.button_ok.setObjectName("button_ok")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.button_ok)
        self.button_cancel = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.button_cancel.setObjectName("button_cancel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button_cancel)
        self.input_name = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.input_name.setObjectName("input_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.input_name)
        self.input_email = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.input_email.setObjectName("input_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.input_email)
        self.input_passwort = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.input_passwort.setObjectName("input_passwort")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.input_passwort)
        self.input_passwort_wdh = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.input_passwort_wdh.setObjectName("input_passwort_wdh")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.input_passwort_wdh)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_email.setText(_translate("MainWindow", "E-Mail"))
        self.label_password.setText(_translate("MainWindow", "Passwort"))
        self.label_passwort_wdh.setText(_translate("MainWindow", "Passwort (Wdh)"))
        self.button_ok.setText(_translate("MainWindow", "Ok"))
        self.button_cancel.setText(_translate("MainWindow", "Cancel"))