from GUI import ARMv8Core
from GUI import armv8_isa
from GUI import instruction
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

	def __init__(self, Core):
       		super(MainWindow, self).__init__()
        	self.initUI()
		self.core = Core
		self.reg_type = 0
	
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
        	self.groupBox.setTitle(_translate("MainWindow", "Registers", None))
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
	

	def run(self):
		
		text = str(self.textEdit.toPlainText())
		
		
		for line in text.splitlines():
			args = line.split()
			####### COMMANDS #################################################################################
        		if args[0] == "help":
            			self.print_instructions()
            			self.print_tips()
        		elif args[0] == "exit":
           			break
            
			####### INSTRUCTIONS ############################################################################
        		elif args[0] == "ADD" :
           			if error_check(args) == 1:
                			armv8_isa.ADD.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "ADDI":
           			 if error_check(args) == 1:
                			armv8_isa.ADDI.execute(self.core, int(args[3]), args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "SUB":
            			if error_check(args) == 1:
                			armv8_isa.SUB.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "SUBI":
            			if error_check(args) == 1:
                			armv8_isa.SUBI.execute(self.core, int(args[3]), args[2], args[1])
               			 	print_all_registers(self.core, self.reg_type)
        		elif args[0] == "MUL":
            			if error_check(args) == 1:
                			armv8_isa.MUL.execute(self.core, args[3], 0x1F, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "UMULH":
            			if error_check(args) == 1:
                			armv8_isa.UMULH.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "SDIV":
            			if error_check(args) == 1:
               				armv8_isa.SDIV.execute(self.core, args[3], 0x02, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "UDIV":
            			if error_check(args) == 1:
                			armv8_isa.UDIV.execute(self.core, args[3], 0x03, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "AND":
            			if error_check(args) == 1:
                			armv8_isa.AND.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "ANDI":
            			if error_check(args) == 1:
                			armv8_isa.ANDI.execute(self.core, int(args[3]), args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "EOR":
            			if error_check(args) == 1:
                			armv8_isa.EOR.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "EORI":
            			if error_check(args) == 1:
                			armv8_isa.EORI.execute(self.core, int(args[3]), args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "LSL":
            			if error_check(args) == 1:
                			armv8_isa.LSL.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "LSR":
           			 if error_check(args) == 1:
                			armv8_isa.LSR.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "ORR":
           			 if error_check(args) == 1:
                			armv8_isa.ORR.execute(self.core, args[3], 0, args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		elif args[0] == "ORRI":
           			 if error_check(args) == 1:
                			armv8_isa.ORRI.execute(self.core, int(args[3]), args[2], args[1])
                			print_all_registers(self.core, self.reg_type)
        		else:
				
            			self.textEdit_2.setText(str(self.textEdit_2.toPlainText()) + "\n Please enter a valid command at line " + line + " . Type 'help' for valid options.\n")
				break
		
	def to_Binary(self):
		self.textEdit_3.setText(print_all_registers(self.core,2))
		self.reg_type = 2

	def to_deci(self):
		self.textEdit_3.setText(print_all_registers(self.core,0))
		self.reg_type = 0

	def to_hex(self):
		self.textEdit_3.setText(print_all_registers(self.core,1))
		self.reg_type = 1


	def print_instructions(self):
		text = str(self.textEdit_2.toPlainText())
    		text += "\n Instructions:"
		text += "  Key:"
   		text +="    Xd = destination register where value is stored\n"
    		text +="    Xn = register where 1st value to be used is stored\n"
    		text +="    Xm = register where 2nd value to be used is stored\n"
   		text += "    d, n, and m must be integers between 0 and 31\n"
    		text += "    SP = stack pointer (can be used in certain instructions in plvace of Xd)\n"
    		text +="    #imm = immediate integer value to be used in insturction (used in place of register and is not stored)\n"
    		text += "  Arithmetic operations:\n"
    		text += "    ADD Xd, Xn, Xm           Add\n"
    		text += "    ADDI Xd, Xn, #imm        Add (immediate)\n"
    		text +="    SUB Xd, Xn, Xm           Subtract\n"
    		text += "    SUBI Xd. Xn, #imm        Subtract (immediate)\n"
    		text +="    MUL Xd, Xn, Xm           Multiply\n"
    		text +="    UMULH Xd, Xn, Xm         Unsigned multiply high\n"
    		text +="    SDIV Xd, Xn, Xm          Signed divide\n"
    		text += "    UDIV Xd. Xn, Xm          Unisnged Divide\n"
    		text +="  Logic operations:\n"
    		text +="    AND Xd, Xn, Xm           Bitwise AND\n"
    		text +="    ANDI Xd|SP, Xn, #imm     Bitwise AND immediate\n"
    		text +="    EOR Xd, Xn, Xm           Bitwise exclusive OR\n"
    		text += "    EORI Xd|SP, Xn, #imm     Bitwise exclusive OR (immediate)\n"
    		text += "    LSL Xd, Xn, Xm|#imm      Logical shift left (register or immediate)\n"
    		text += "    LSR Xd, Xn, Xm|#imm      Logical shift right (register or immediate)\n"
    		text += "    ORR Xd, Xn, Xm           Bitwise inclusive OR\n"
    		text += "    ORRI Xd|SP, Xn, #imm     Bitwise inclusive OR (immediate)\n"
    		text += "\n"
		self.textEdit_2.setText(text) 
    
	def print_tips(self):
		text = str(self.textEdit_2.toPlainText())
    		text +=  "Tips:\n"
    		text += "  Checkout http://armsim.cs.uvic.ca/ for another ARM simulation tool\n"
    		text += "\n"
		self.textEdit_2.setText(text) 
    


	
def main():
	core  = ARMv8Core()
	print_all_registers(core,0)
	print_all_registers(core,1)
	print_all_registers(core,2)
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow(core)
	mw.to_deci()
	mw.show()
	sys.exit(app.exec_())

def print_register(register, core, bin_hex_deci):
	if(bin_hex_deci == 0):
		return  str(register) + " = " + str(core.reg[register].get()) + "\n"
	elif(bin_hex_deci == 1):
		return  str(register) + " = " + str(hex(core.reg[register].get()))+ "\n"
	else:
		return  str(register) + " = " + str(bin(core.reg[register].get()))+ "\n"
    
def print_all_registers(core, bin_hex_deci):
	reg_str = ""
	for num in range(0,31):
		register = "X" + str(num)
		reg_str = reg_str + print_register(register, core, bin_hex_deci) + "----------------------------------- \n"
	reg_str = reg_str + print_register("XZR", core, bin_hex_deci) + "\n"
	return reg_str
	
def error_check(args):
	if(len(args)< 4 or "//" in args[0] or "//" in args[1] or "//" in args[2] or "//" in args[3]  ):
		print "change to print to output log"
		print "Error: incorrect number of arguments. \n Instructions should have the following format: \n eg. ADD X2 X0 X1 or ADDI X3 X2 2 \n"
		return -1
	else:
		return 1
 
