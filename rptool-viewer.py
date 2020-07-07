# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from core.rptool import RPTool

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tabRPTool = QtWidgets.QWidget()
        self.tabRPTool.setObjectName("tabRPTool")

        # List Widget Test Cases
        self.lvTestCases = QtWidgets.QListWidget(self.tabRPTool)
        self.lvTestCases.setGeometry(QtCore.QRect(10, 60, 641, 271))
        self.lvTestCases.setObjectName("lvTestCases")
        self.lvTestCases.itemClicked.connect(self.itemSelected)

        # Button 'rec'
        self.pbRec = QtWidgets.QPushButton(self.tabRPTool)
        self.pbRec.setGeometry(QtCore.QRect(10, 340, 41, 25))
        self.pbRec.setObjectName("pbRec")
        self.pbRec.clicked.connect(self.addTestCase)

        self.leTestCaseName = QtWidgets.QLineEdit(self.tabRPTool)
        self.leTestCaseName.setGeometry(QtCore.QRect(10, 30, 301, 25))
        self.leTestCaseName.setObjectName("leTestCaseName")
        self.leTestFolder = QtWidgets.QLineEdit(self.tabRPTool)
        self.leTestFolder.setGeometry(QtCore.QRect(320, 30, 331, 25))
        self.leTestFolder.setObjectName("leTestFolder")
        self.lblTestCaseName = QtWidgets.QLabel(self.tabRPTool)
        self.lblTestCaseName.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.lblTestCaseName.setObjectName("lblTestCaseName")
        self.lblTestFolder = QtWidgets.QLabel(self.tabRPTool)
        self.lblTestFolder.setGeometry(QtCore.QRect(320, 10, 71, 17))
        self.lblTestFolder.setObjectName("lblTestFolder")

        self.pbPlay = QtWidgets.QPushButton(self.tabRPTool)
        self.pbPlay.setGeometry(QtCore.QRect(60, 340, 51, 25))
        self.pbPlay.setObjectName("pbPlay")
        self.pbPlay.setEnabled(False)
        self.pbPlay.clicked.connect(self.playTestCase)

        self.pbDelete = QtWidgets.QPushButton(self.tabRPTool)
        self.pbDelete.setGeometry(QtCore.QRect(180, 340, 51, 25))
        self.pbDelete.setObjectName("pbDelete")
        self.pbDelete.setEnabled(False)
        self.pbDelete.clicked.connect(self.deleteTestCase)

        self.pbPlayAll = QtWidgets.QPushButton(self.tabRPTool)
        self.pbPlayAll.setGeometry(QtCore.QRect(120, 340, 51, 25))
        self.pbPlayAll.setObjectName("pbPlayAll")
        self.pbPlayAll.setEnabled(False)

        self.lblToolStatus = QtWidgets.QLabel(self.tabRPTool)
        self.lblToolStatus.setGeometry(QtCore.QRect(250, 330, 371, 41))
        self.lblToolStatus.setObjectName("lblToolStatus")
        self.tabWidget.addTab(self.tabRPTool, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.pbSaveSettings = QtWidgets.QPushButton(self.tabSettings)
        self.pbSaveSettings.setGeometry(QtCore.QRect(10, 330, 61, 25))
        self.pbSaveSettings.setObjectName("pbSaveSettings")
        self.lblUsername = QtWidgets.QLabel(self.tabSettings)
        self.lblUsername.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.lblUsername.setObjectName("lblUsername")
        self.lblTestlinkApiKey = QtWidgets.QLabel(self.tabSettings)
        self.lblTestlinkApiKey.setGeometry(QtCore.QRect(310, 10, 111, 17))
        self.lblTestlinkApiKey.setObjectName("lblTestlinkApiKey")
        self.leUsername = QtWidgets.QLineEdit(self.tabSettings)
        self.leUsername.setGeometry(QtCore.QRect(10, 30, 291, 25))
        self.leUsername.setObjectName("leUsername")
        self.leTestlinkApiKey = QtWidgets.QLineEdit(self.tabSettings)
        self.leTestlinkApiKey.setGeometry(QtCore.QRect(310, 30, 341, 25))
        self.leTestlinkApiKey.setObjectName("leTestlinkApiKey")
        self.cbProjects = QtWidgets.QComboBox(self.tabSettings)
        self.cbProjects.setGeometry(QtCore.QRect(10, 150, 291, 25))
        self.cbProjects.setObjectName("cbProjects")
        self.leTestlinkAddress = QtWidgets.QLineEdit(self.tabSettings)
        self.leTestlinkAddress.setGeometry(QtCore.QRect(10, 90, 641, 25))
        self.leTestlinkAddress.setObjectName("leTestlinkAddress")
        self.lblTestlinkAddress = QtWidgets.QLabel(self.tabSettings)
        self.lblTestlinkAddress.setGeometry(QtCore.QRect(10, 70, 101, 17))
        self.lblTestlinkAddress.setObjectName("lblTestlinkAddress")
        self.pbConnect = QtWidgets.QPushButton(self.tabSettings)
        self.pbConnect.setGeometry(QtCore.QRect(80, 330, 80, 25))
        self.pbConnect.setObjectName("pbConnect")
        self.lblSettingsStatus = QtWidgets.QLabel(self.tabSettings)
        self.lblSettingsStatus.setGeometry(QtCore.QRect(180, 330, 171, 21))
        self.lblSettingsStatus.setObjectName("lblSettingsStatus")
        self.lblTestProject = QtWidgets.QLabel(self.tabSettings)
        self.lblTestProject.setGeometry(QtCore.QRect(10, 120, 91, 31))
        self.lblTestProject.setObjectName("lblTestProject")
        self.cbPlans = QtWidgets.QComboBox(self.tabSettings)
        self.cbPlans.setGeometry(QtCore.QRect(310, 150, 341, 25))
        self.cbPlans.setObjectName("cbPlans")
        self.lblTestPlan = QtWidgets.QLabel(self.tabSettings)
        self.lblTestPlan.setGeometry(QtCore.QRect(310, 126, 91, 21))
        self.lblTestPlan.setObjectName("lblTestPlan")
        self.cbPlatforms = QtWidgets.QComboBox(self.tabSettings)
        self.cbPlatforms.setGeometry(QtCore.QRect(10, 210, 291, 25))
        self.cbPlatforms.setObjectName("cbPlatforms")
        self.cbBuilds = QtWidgets.QComboBox(self.tabSettings)
        self.cbBuilds.setGeometry(QtCore.QRect(310, 210, 341, 25))
        self.cbBuilds.setObjectName("cbBuilds")
        self.lblPlatform = QtWidgets.QLabel(self.tabSettings)
        self.lblPlatform.setGeometry(QtCore.QRect(10, 186, 91, 21))
        self.lblPlatform.setObjectName("lblPlatform")
        self.lblBuild = QtWidgets.QLabel(self.tabSettings)
        self.lblBuild.setGeometry(QtCore.QRect(310, 186, 54, 21))
        self.lblBuild.setObjectName("lblBuild")
        self.tabWidget.addTab(self.tabSettings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # RPTool init
        self.rpt = RPTool()
        self.setFolderDir()
        self.listTests()


    def setFolderDir(self):
        self.leTestFolder.setText(self.rpt.getTestFolder())

    def listTests(self):
        for test in self.rpt.getTestFiles():
            print (test)
            self.lvTestCases.addItem(test)

    def addTestCase(self):
        tc_name = self.leTestCaseName.text()
        self.leTestCaseName.setText('')
        self.lvTestCases.addItem(tc_name)
        self.rpt.rec(tc_name)

    def itemSelected(self, item):
        print('selected ', item.text())
        self.tcItem = item
        self.pbRec.setEnabled(False)
        self.pbPlay.setEnabled(True)
        self.pbDelete.setEnabled(True)

    def deleteTestCase(self):
        print('deleting ', self.tcItem.text())
        self.lvTestCases.takeItem(self.lvTestCases.currentRow())
        self.rpt.delete(self.tcItem.text())
        self.pbRec.setEnabled(True)
        self.pbPlay.setEnabled(False)

    def playTestCase(self):
        print('playing ', self.tcItem.text())
        self.pbRec.setEnabled(True)
        self.pbPlay.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPTool Viewer"))
        self.pbRec.setText(_translate("MainWindow", "Rec"))
        self.lblTestCaseName.setText(_translate("MainWindow", "Test Case Name"))
        self.lblTestFolder.setText(_translate("MainWindow", "Test Folder"))
        self.pbPlay.setText(_translate("MainWindow", "Play"))
        self.pbDelete.setText(_translate("MainWindow", "Del"))
        self.pbPlayAll.setText(_translate("MainWindow", "Play All"))
        self.lblToolStatus.setText(_translate("MainWindow", "Not started yet!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRPTool), _translate("MainWindow", "RPTool"))
        self.pbSaveSettings.setText(_translate("MainWindow", "Save"))
        self.lblUsername.setText(_translate("MainWindow", "Username"))
        self.lblTestlinkApiKey.setText(_translate("MainWindow", "Testlink API KEY"))
        self.lblTestlinkAddress.setText(_translate("MainWindow", "Testlink Address"))
        self.pbConnect.setText(_translate("MainWindow", "Connect"))
        self.lblSettingsStatus.setText(_translate("MainWindow", "Not connected"))
        self.lblTestProject.setText(_translate("MainWindow", "Test Projects"))
        self.lblTestPlan.setText(_translate("MainWindow", "Test Plans"))
        self.lblPlatform.setText(_translate("MainWindow", "Platforms"))
        self.lblBuild.setText(_translate("MainWindow", "Builds"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
