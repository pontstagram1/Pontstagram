# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PIL import Image, ImageQt
import filtres_photos

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

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(500, 500)
		Dialog.setSizeGripEnabled(True)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(100, 350, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(30, 10, 391, 301))
		self.label.setScaledContents(True)
		self.label.setObjectName(_fromUtf8("label"))
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(20, 360, 75, 23))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(100, 360, 75, 23))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		
	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.label.setText(_translate("Dialog", "TextLabel", None))
		self.pushButton.setText(_translate("Dialog", "Browse", None))
		self.pushButton_2.setText(_translate("Dialog", "filtre1", None))
  
import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
ui.Original = Image.new("RGB",(15,10)) # Image initiale en PIL

def print_image (image):
	ui.temp = ImageQt.ImageQt(image) # format ImageQt
	ui.affichage = QtGui.QPixmap.fromImage(ui.temp) # format QPixmap
	if ui.affichage.height()<ui.affichage.width() :
		ui.label.setGeometry(QtCore.QRect(30, 30, 440, 440*ui.affichage.height()/ui.affichage.width()))
	else :
		ui.label.setGeometry(QtCore.QRect(30, 30, 440*ui.affichage.width()/ui.affichage.height(), 440))
	ui.label.setPixmap(ui.affichage)

def selectFile():
	adresse=str(QtGui.QFileDialog.getOpenFileName())
	ui.Original=Image.open(adresse,"r")	# format PIL
	print_image(ui.Original)
	
QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), selectFile)

def appliquer_filtre1():
	print_image(filtres_photos.test1(ui.Original))
	
QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), appliquer_filtre1)
    
if __name__ == "__main__":
    Dialog.show()
    sys.exit(app.exec_())

