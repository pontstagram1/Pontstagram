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
		Dialog.resize(500, 600)
		Dialog.setMaximumSize(500,600)
		Dialog.setMinimumSize(500,600)
		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(30, 10, 391, 301))
		self.label.setScaledContents(True)
		self.label.setObjectName(_fromUtf8("label"))
		self.label_2 = QtGui.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(100, 0, 300, 30))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.label_2.setAlignment( QtCore.Qt.AlignCenter )
		self.scrollArea = QtGui.QScrollArea(Dialog)
		self.scrollArea.setGeometry(QtCore.QRect(0, 512, 500, 61))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents_2 = QtGui.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 93, 52))
		self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(30, 574, 74, 22))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
		self.pushButton_1 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
		self.horizontalLayout_3.addWidget(self.pushButton_1)
		self.pushButton_1.setEnabled(False)
		self.pushButton_save = QtGui.QPushButton(Dialog)
		self.pushButton_save.setGeometry(QtCore.QRect(213, 574, 74, 22))
		self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
		self.pushButton_save.setEnabled(False)
		self.pushButton_quit = QtGui.QPushButton(Dialog)
		self.pushButton_quit.setGeometry(QtCore.QRect(396, 574, 74, 22))
		self.pushButton_quit.setObjectName(_fromUtf8("pushButton_quit"))
		self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.horizontalLayout_3.addWidget(self.pushButton_2)
		self.pushButton_2.setEnabled(False)
		self.horizontalSlider = QtGui.QSlider(Dialog)
		self.horizontalSlider.setGeometry(QtCore.QRect(30, 490, 440, 20))
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
		self.horizontalSlider.setEnabled(False)
		self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.horizontalLayout_3.addWidget(self.pushButton_3)
		self.pushButton_3.setEnabled(False)
		self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.horizontalLayout_3.addWidget(self.pushButton_4)
		self.pushButton_4.setEnabled(False)
		self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.horizontalLayout_3.addWidget(self.pushButton_5)
		self.pushButton_5.setEnabled(False)
		self.pushButton_6 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		self.horizontalLayout_3.addWidget(self.pushButton_6)
		self.pushButton_6.setEnabled(False)
		self.pushButton_7 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.horizontalLayout_3.addWidget(self.pushButton_7)
		self.pushButton_7.setEnabled(False)
		self.pushButton_8 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.horizontalLayout_3.addWidget(self.pushButton_8)
		self.pushButton_8.setEnabled(False)
		self.pushButton_9 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.horizontalLayout_3.addWidget(self.pushButton_9)
		self.pushButton_9.setEnabled(False)
		self.pushButton_10 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
		self.horizontalLayout_3.addWidget(self.pushButton_10)
		self.pushButton_10.setEnabled(False)
		self.pushButton_11 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.horizontalLayout_3.addWidget(self.pushButton_11)
		self.pushButton_11.setEnabled(False)
		self.pushButton_12 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
		self.horizontalLayout_3.addWidget(self.pushButton_12)
		self.pushButton_12.setEnabled(False)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.pushButton_quit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		
	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Ponstagram by IMInulati", None))
		self.label.setText(_translate("Dialog", "", None))
		self.pushButton.setText(_translate("Dialog", "Ouvrir", None))
		self.pushButton_1.setText(_translate("Dialog", "Aube", None))
		self.pushButton_2.setText(_translate("Dialog", "Contraste", None))
		self.pushButton_save.setText(_translate("Dialog", "Enregistrer", None))
		self.pushButton_quit.setText(_translate("Dialog", "Quitter", None))
		self.pushButton_3.setText(_translate("Dialog", "Nostalgie", None))
		self.pushButton_4.setText(_translate("Dialog", "Binary", None))
		self.pushButton_5.setText(_translate("Dialog", "Amaro", None))
		self.pushButton_6.setText(_translate("Dialog", "Vieux", None))
		self.pushButton_7.setText(_translate("Dialog", "Amour gloire et beaute", None))
		self.pushButton_8.setText(_translate("Dialog", "Printemps nucleaire", None))
		self.pushButton_9.setText(_translate("Dialog", "Luminosite", None))
		self.pushButton_10.setText(_translate("Dialog", "Bruit", None))
		self.pushButton_11.setText(_translate("Dialog", "Flou", None))
		self.pushButton_12.setText(_translate("Dialog", "Sepia", None))
  
import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
ui.Original = Image.new("RGB",(1,1)) # Image initiale en PIL
ui.Original_petit = Image.new("RGB",(1,1)) # Image plus petite pour accélérer les visualisations temporaires
ui.filtre_utilise = 0
ui.label.setGeometry(75,152,350,196)
ui.label.setPixmap(QtGui.QPixmap("logo.png"))


def selectFile():
	ui.filtre_utilise = 0
	adresse=str(QtGui.QFileDialog.getOpenFileName())
	if(adresse!=""):
		ui.label_2.setText("Chargement image...")
		ui.Original=Image.open(adresse,"r")	# format PIL
		if(ui.Original.size[1]<ui.Original.size[0]):
			ui.Original_petit=ui.Original.resize((440,ui.Original.size[1]*440/ui.Original.size[0]))
		else:
			ui.Original_petit=ui.Original.resize((ui.Original.size[0]*440/ui.Original.size[1],440))
		print_image(ui.Original_petit)
		ui.pushButton_save.setEnabled(True)
		ui.pushButton_1.setEnabled(True)
		ui.pushButton_2.setEnabled(True)
		ui.pushButton_3.setEnabled(True)
		ui.pushButton_4.setEnabled(True)
		ui.pushButton_5.setEnabled(True)
		ui.pushButton_6.setEnabled(True)
		ui.pushButton_7.setEnabled(True)
		ui.pushButton_8.setEnabled(True)
		ui.pushButton_9.setEnabled(True)
		ui.pushButton_10.setEnabled(True)
		ui.pushButton_11.setEnabled(True)
		ui.pushButton_12.setEnabled(True)
		ui.label_2.setText("Image chargee!")

ui.fonction_slider=selectFile
	
def print_image (image):
	ui.temp = ImageQt.ImageQt(image.convert("RGB")) # format ImageQt
	ui.affichage = QtGui.QPixmap.fromImage(ui.temp) # format QPixmap
	if ui.affichage.height()<ui.affichage.width() :
		ui.label.setGeometry(QtCore.QRect(30, 250-220*ui.affichage.height()/ui.affichage.width(), 440, 440*ui.affichage.height()/ui.affichage.width()))
	else :
		ui.label.setGeometry(QtCore.QRect(250-220*ui.affichage.width()/ui.affichage.height(), 30, 440*ui.affichage.width()/ui.affichage.height(), 440))
	ui.label.setPixmap(ui.affichage)

def appliquer_aube():
	Dialog.show()
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 1
	print_image(filtres_photos.aube(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def appliquer_contraste():
	print_image(ui.Original_petit)
	ui.horizontalSlider.setEnabled(True)
	if (ui.fonction_slider!=selectFile) :
		QtCore.QObject.disconnect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.fonction_slider=appliquer_contraste_value
	ui.horizontalSlider.setValue(50)
	QtCore.QObject.connect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.label_2.setText("Modifiez la position du curseur...")

def appliquer_contraste_value():
	ui.filtre_utilise = 2
	ui.A=ui.horizontalSlider.sliderPosition()*ui.horizontalSlider.sliderPosition()/float(2500)
	print_image(filtres_photos.contraste(ui.Original_petit,ui.A,ui.A,ui.A))

def appliquer_nostalgie():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 3
	print_image(filtres_photos.nostalgie(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")

def appliquer_binary():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 4
	print_image(filtres_photos.binary(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def appliquer_amaro():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 5
	print_image(filtres_photos.amaro(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def appliquer_filtre_vieux():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 6
	print_image(filtres_photos.filtre_vieux(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def appliquer_amour_gloire_et_beaute():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 7
	print_image(filtres_photos.amour_gloire_et_beaute(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def appliquer_printemps_nucleaire():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 8
	print_image(filtres_photos.printemps_nucleaire(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def appliquer_luminosite():
	print_image(ui.Original_petit)
	ui.horizontalSlider.setEnabled(True)
	if (ui.fonction_slider!=selectFile) :
		QtCore.QObject.disconnect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.fonction_slider=appliquer_luminosite_value
	ui.horizontalSlider.setValue(50)
	QtCore.QObject.connect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.label_2.setText("Modifiez la position du curseur...")

def appliquer_luminosite_value():
	ui.filtre_utilise = 9
	ui.A=2*(50-ui.horizontalSlider.sliderPosition())
	print_image(filtres_photos.luminosite(ui.Original_petit,ui.A))

def appliquer_bruit():
	print_image(ui.Original_petit)
	ui.horizontalSlider.setEnabled(True)
	if (ui.fonction_slider!=selectFile) :
		QtCore.QObject.disconnect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.fonction_slider=appliquer_bruit_value
	ui.horizontalSlider.setValue(0)
	QtCore.QObject.connect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.label_2.setText("Modifiez la position du curseur...")

def appliquer_bruit_value():
	ui.filtre_utilise = 10
	ui.A=(ui.horizontalSlider.sliderPosition())/float(50)
	print_image(filtres_photos.bruit(ui.Original_petit,ui.A))
	
def appliquer_flou():
	print_image(ui.Original_petit)
	ui.horizontalSlider.setEnabled(True)
	if (ui.fonction_slider!=selectFile) :
		QtCore.QObject.disconnect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.fonction_slider=appliquer_flou_value
	ui.horizontalSlider.setValue(0)
	QtCore.QObject.connect(ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), ui.fonction_slider)
	ui.label_2.setText("Modifiez la position du curseur...")

def appliquer_flou_value():
	ui.filtre_utilise = 11
	ui.A=(ui.horizontalSlider.sliderPosition())/float(35)
	print_image(filtres_photos.flou(ui.Original_petit,ui.A))
	
def appliquer_sepia():
	ui.horizontalSlider.setEnabled(False)
	ui.filtre_utilise = 12
	print_image(filtres_photos.sepia(ui.Original_petit))
	ui.label_2.setText("Filtre applique!")
	
def enregistrer():
	if ui.filtre_utilise==0:
		ui.label_2.setText("L'image n'a pas ete modifiee... o.O")
		return None
	s=str(QtGui.QFileDialog.getSaveFileName())
	if(s!=""):
		if ui.filtre_utilise==1:
			(filtres_photos.aube(ui.Original)).save(s)
		elif ui.filtre_utilise==2:
			(filtres_photos.contraste(ui.Original,ui.A,ui.A,ui.A)).save(s)
		elif ui.filtre_utilise==3:
			(filtres_photos.nostalgie(ui.Original)).save(s)
		elif ui.filtre_utilise==4:
			(filtres_photos.binary(ui.Original)).save(s)
		elif ui.filtre_utilise==5:
			(filtres_photos.amaro(ui.Original)).save(s)
		elif ui.filtre_utilise==6:
			(filtres_photos.filtre_vieux(ui.Original)).save(s)
		elif ui.filtre_utilise==7:
			(filtres_photos.amour_gloire_et_beaute(ui.Original)).save(s)
		elif ui.filtre_utilise==8:
			(filtres_photos.printemps_nucleaire(ui.Original)).save(s)
		elif ui.filtre_utilise==9:
			(filtres_photos.luminosite(ui.Original,ui.A)).save(s)
		elif ui.filtre_utilise==10:
			(filtres_photos.bruit(ui.Original,ui.A)).save(s)
		elif ui.filtre_utilise==11:
			(filtres_photos.flou(ui.Original,ui.A)).save(s)
		elif ui.filtre_utilise==12:
			(filtres_photos.sepia(ui.Original)).save(s)
		ui.label_2.setText("Image enregistree!")
	else:
		ui.label_2.setText("Enregistrement annule...")
def text_filtre():
	ui.label_2.setText("Patientez, application du filtre...")

def text_enregistrer():
	ui.label_2.setText("Patientez, application du filtre puis enregistrement...")

QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), selectFile)
QtCore.QObject.connect(ui.pushButton_save, QtCore.SIGNAL(_fromUtf8("released()")), enregistrer)
QtCore.QObject.connect(ui.pushButton_save, QtCore.SIGNAL(_fromUtf8("pressed()")), text_enregistrer)
QtCore.QObject.connect(ui.pushButton_1, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_aube)
QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_contraste)
QtCore.QObject.connect(ui.pushButton_3, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_nostalgie)
QtCore.QObject.connect(ui.pushButton_4, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_binary)
QtCore.QObject.connect(ui.pushButton_5, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_amaro)
QtCore.QObject.connect(ui.pushButton_6, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_filtre_vieux)
QtCore.QObject.connect(ui.pushButton_7, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_amour_gloire_et_beaute)
QtCore.QObject.connect(ui.pushButton_8, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_printemps_nucleaire)
QtCore.QObject.connect(ui.pushButton_9, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_luminosite)
QtCore.QObject.connect(ui.pushButton_10, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_bruit)
QtCore.QObject.connect(ui.pushButton_11, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_flou)
QtCore.QObject.connect(ui.pushButton_12, QtCore.SIGNAL(_fromUtf8("released()")), appliquer_sepia)
QtCore.QObject.connect(ui.pushButton_1, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_3, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_4, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_5, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_6, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_7, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_8, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
QtCore.QObject.connect(ui.pushButton_12, QtCore.SIGNAL(_fromUtf8("pressed()")), text_filtre)
	
if __name__ == "__main__":
	Dialog.show()
	sys.exit(app.exec_())

