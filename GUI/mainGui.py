import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s




try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class MainWindow(QtGui.QMainWindow):

	def __init__(self, Regis):
       		super(MainWindow, self).__init__()
        	self.Regi_List = Regis
        	self.initUI()
        
        
	def initUI(self):               
        	self.setObjectName(_fromUtf8("MainWindow"))
        	self.resize(794, 600)
        	self.centralwidget = QtGui.QWidget(self)
        	self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        	self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        	self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 614))
        	self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        	self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
       		self.gridLayout.setMargin(10)
        	self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        	self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        	self.groupBox.setObjectName(_fromUtf8("groupBox"))
        	self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        	self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        	self.pushButton = QtGui.QPushButton(self.groupBox)
        	self.pushButton.setObjectName(_fromUtf8("pushButton"))
        	self.verticalLayout.addWidget(self.pushButton)
        	self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        	self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        	self.verticalLayout.addWidget(self.pushButton_2)
        	self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        	self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        	self.verticalLayout.addWidget(self.pushButton_3)
        	self.textEdit_3 = QtGui.QTextEdit(self.groupBox)
       		self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
		self.textEdit_3.setReadOnly(True)
        	self.verticalLayout.addWidget(self.textEdit_3)
        	self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        	self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        	self.textEdit.setObjectName(_fromUtf8("textEdit"))
        	self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        	self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        	self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        	self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        	self.textEdit_2 = QtGui.QTextEdit(self.gridLayoutWidget)
        	self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
		self.textEdit_2.setReadOnly(True)
        	self.gridLayout.addWidget(self.textEdit_2, 2, 0, 1, 2)
        	self.groupBox_2 = QtGui.QGroupBox(self.gridLayoutWidget)
        	self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        	self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        	self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        	self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        	self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        

        	self.horizontalLayout.addWidget(self.pushButton_5)
        	self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        	self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        	self.horizontalLayout.addWidget(self.pushButton_6)
        	self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        	self.setCentralWidget(self.centralwidget)
        	self.menubar = QtGui.QMenuBar(self)
        	self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 25))
        	self.menubar.setObjectName(_fromUtf8("menubar"))
        	self.menuFile = QtGui.QMenu(self.menubar)
        	self.menuFile.setObjectName(_fromUtf8("menuFile"))
        	self.menuRun = QtGui.QMenu(self.menubar)
        	self.menuRun.setObjectName(_fromUtf8("menuRun"))
        	self.setMenuBar(self.menubar)
        	self.statusbar = QtGui.QStatusBar(self)
        	self.statusbar.setObjectName(_fromUtf8("statusbar"))
        	self.setStatusBar(self.statusbar)
        	self.actionOpen = QtGui.QAction(self)
        	self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        	self.actionSave = QtGui.QAction(self)
        	self.actionSave.setObjectName(_fromUtf8("actionSave"))
        	self.actionExit = QtGui.QAction(self)
        	self.actionExit.setObjectName(_fromUtf8("actionExit"))
        	self.menuFile.addAction(self.actionOpen)
        	self.menuFile.addAction(self.actionSave)
        	self.menuFile.addAction(self.actionExit)
       		self.menubar.addAction(self.menuFile.menuAction())
        	self.menubar.addAction(self.menuRun.menuAction())
		self.retranslateUi()
	

	def retranslateUi(self):
       		self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        	self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        	self.pushButton.setText(_translate("MainWindow", "Decimal", None))
		self.pushButton.clicked.connect(self.to_deci)

        	self.pushButton_2.setText(_translate("MainWindow", "Hexidecimal", None))
		self.pushButton_2.clicked.connect(self.to_hex)

        	self.pushButton_3.setText(_translate("MainWindow", "binary", None))
		self.pushButton_3.clicked.connect(self.to_Binary)

        	self.pushButton_4.setText(_translate("MainWindow", "Run", None))
		self.pushButton_4.clicked.connect(self.run)


        	self.groupBox_2.setTitle(_translate("MainWindow", "File", None))


        	self.pushButton_5.setText(_translate("MainWindow", "Open", None))
		self.pushButton_5.clicked.connect(self.showDialog)



        	self.pushButton_6.setText(_translate("MainWindow", "Save", None))
		self.pushButton_6.clicked.connect(self.saveData)

        	self.menuFile.setTitle(_translate("MainWindow", "File", None))
        	self.menuRun.setTitle(_translate("MainWindow", "Run", None))
        	self.actionOpen.setText(_translate("MainWindow", "Open", None))
        	self.actionSave.setText(_translate("MainWindow", "Save", None))
        	self.actionExit.setText(_translate("MainWindow", "Exit", None))



	def showDialog(self):

        	fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        
        	f = open(fname, 'r')
        
       		with f:        
           		data = f.read()
            		self.textEdit.setText(data) 
	
	def saveData(self):
 		name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        	file = open(name,'w')
        	text = self.textEdit.toPlainText()
        	file.write(text)
        	file.close() 
	
	def outputLog(self, text):
		b = 0
        	#print some new text to the log
		#self.textEdit_3.SETTEXT

	def run(self):
		b= 0
		
	def to_Binary(self):
		txt = "Registers In Binary: \n"
		for i in range(len(self.Regi_List)):
			txt += "Register " + str(i) + " : " + str( int(bin(self.Regi_List[i])[2:])) + "\n"
		
		self.textEdit_3.setText(txt)


	def to_deci(self):
		txt = "Registers In Deci: \n"
		for i in range(len(self.Regi_List)):
			txt += "Register " + str(i) + " : " + str(self.Regi_List[i]) + "\n"
		self.textEdit_3.setText(txt)


	def to_hex(self):
		txt = "Registers In Hexidecimal: \n"
		for i in range(len(self.Regi_List)):
			txt += "Register " + str(i) + " : " + str( hex(self.Regi_List[i])) + "\n"
		
		self.textEdit_3.setText(txt)
		

	def outputRegis(self, Regis):
		for i in range(len(Regis)):
			self.Regi_List[i] = Regis[i]
        

	def update_Regis(self,regis):
		self.Regi_List = Regis
	
def main():
    r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow(r)
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
