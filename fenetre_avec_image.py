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
		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(30, 10, 391, 301))
		self.label.setScaledContents(True)
		self.label.setObjectName(_fromUtf8("label"))
		self.scrollArea = QtGui.QScrollArea(Dialog)
		self.scrollArea.setGeometry(QtCore.QRect(160, 90, 71, 71))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents_2 = QtGui.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 93, 52))
		self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.horizontalLayout_3.addWidget(self.pushButton)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
		self.pushButton_1 = QtGui.QPushButton(Dialog)
		self.pushButton_1.setGeometry(QtCore.QRect(100, 360, 75, 23))
		self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
		self.pushButton_save = QtGui.QPushButton(Dialog)
		self.pushButton_save.setGeometry(QtCore.QRect(150, 360, 75, 23))
		self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
		self.pushButton_quit = QtGui.QPushButton(Dialog)
		self.pushButton_quit.setGeometry(QtCore.QRect(200, 360, 75, 23))
		self.pushButton_quit.setObjectName(_fromUtf8("pushButton_quit"))
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(100, 400, 75, 23))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.verticalSlider = QtGui.QSlider(Dialog)
		self.verticalSlider.setGeometry(QtCore.QRect(80, 70, 19, 160))
		self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
		self.verticalSlider.setEnabled(False)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.pushButton_quit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		
	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.label.setText(_translate("Dialog", "", None))
		self.pushButton.setText(_translate("Dialog", "Ouvrir", None))
		self.pushButton_1.setText(_translate("Dialog", "filtre1", None))
		self.pushButton_2.setText(_translate("Dialog", "contraste", None))
		self.pushButton_save.setText(_translate("Dialog", "Enregistrer", None))
		self.pushButton_quit.setText(_translate("Dialog", "Quitter", None))
  
import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
ui.Original = Image.new("RGB",(1,1)) # Image initiale en PIL
ui.Original_petit = Image.new("RGB",(1,1)) # Image plus petite pour accélérer les visualisations temporaires
ui.filtre_utilise = 0


def selectFile():
	ui.filtre_utilise = 0
	adresse=str(QtGui.QFileDialog.getOpenFileName())
	ui.Original=Image.open(adresse,"r")	# format PIL
	if(ui.Original.size[1]<ui.Original.size[0]):
		ui.Original_petit=ui.Original.resize((440,ui.Original.size[1]*440/ui.Original.size[0]))
	else:
		ui.Original_petit=ui.Original.resize((340,ui.Original.size[1]*340/ui.Original.size[0]))
	print_image(ui.Original_petit)

ui.fonction_slider=selectFile
	
def print_image (image):
	ui.temp = ImageQt.ImageQt(image) # format ImageQt
	ui.affichage = QtGui.QPixmap.fromImage(ui.temp) # format QPixmap
	if ui.affichage.height()<ui.affichage.width() :
		ui.label.setGeometry(QtCore.QRect(30, 30, 440, 440*ui.affichage.height()/ui.affichage.width()))
	else :
		ui.label.setGeometry(QtCore.QRect(250-170*ui.affichage.width()/ui.affichage.height(), 30, 340*ui.affichage.width()/ui.affichage.height(), 340))
	ui.label.setPixmap(ui.affichage)

def appliquer_filtre1():
        ui.verticalSlider.setEnabled(False)
        ui.filtre_utilise = 1
        print_image(filtres_photos.aube(ui.Original_petit))
	
def appliquer_contraste():
	ui.verticalSlider.setEnabled(True)
	if (ui.fonction_slider!=selectFile) :
		QtCore.QObject.disconnect(ui.verticalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.fonction_slider=appliquer_contraste_value
	ui.verticalSlider.setValue(50)
	QtCore.QObject.connect(ui.verticalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)

def appliquer_contraste_value():
	ui.filtre_utilise = 2
	ui.A=ui.verticalSlider.sliderPosition()*ui.verticalSlider.sliderPosition()/float(2500)
	print_image(filtres_photos.contraste(ui.Original_petit,ui.A,ui.A,ui.A))

def enregistrer():
	if ui.filtre_utilise==0:
		print "L'image n'a pas ete modifiee"
		return None
	s=str(QtGui.QFileDialog.getSaveFileName())
	if ui.filtre_utilise==1:
		(filtres_photos.aube(ui.Original)).save(s)
	if ui.filtre_utilise==2:
		(filtres_photos.contraste(ui.Original,ui.A,ui.A,ui.A)).save(s)

QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), selectFile)
QtCore.QObject.connect(ui.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), appliquer_filtre1)
QtCore.QObject.connect(ui.pushButton_save, QtCore.SIGNAL(_fromUtf8("clicked()")), enregistrer)
QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), appliquer_contraste)
	
if __name__ == "__main__":
	Dialog.show()
	sys.exit(app.exec_())

