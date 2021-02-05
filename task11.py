# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cyborg.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



import numpy as np
import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QHBoxLayout,QFileDialog,QMessageBox
location=" "
from PIL import Image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(983, 731)
        self.browse = QtWidgets.QPushButton(Dialog)
        self.browse.setGeometry(QtCore.QRect(100, 550, 191, 71))
        self.browse.setObjectName("browse")
        self.convert = QtWidgets.QPushButton(Dialog)
        self.convert.setGeometry(QtCore.QRect(710, 550, 191, 71))
        self.convert.setObjectName("convert")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 100, 321, 321))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.image_2 = QtWidgets.QLabel(Dialog)
        self.image_2.setGeometry(QtCore.QRect(600, 100, 321, 321))
        self.image_2.setScaledContents(True)
        self.image_2.setObjectName("image_2")
        self.download_location = QtWidgets.QPushButton(Dialog)
        self.download_location.setGeometry(QtCore.QRect(390, 550, 191, 71))
        self.download_location.setObjectName("download_location")
        self.location = QtWidgets.QLineEdit(Dialog)
        self.location.setGeometry(QtCore.QRect(360, 490, 261, 41))
        self.location.setObjectName("location")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.browse.clicked.connect(self.openFileDialog)
        self.convert.clicked.connect(self.convertFile)
        self.download_location.clicked.connect(self.browsefiles)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.browse.setText(_translate("Dialog", "Browse"))
        self.convert.setText(_translate("Dialog", "Convert and Save"))
        self.label.setText(_translate("Dialog", "                            Image 1"))
        self.image_2.setText(_translate("Dialog", "                              Image 2"))
        self.download_location.setText(_translate("Dialog", "Click to set the save location"))


    def openFileDialog(self):
        global location
        option=QFileDialog.Options()
        widget=QWidget()
        file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Images (*.png, *.xmp *.jpg)',options=option)
        self.label.setPixmap(QtGui.QPixmap(file[0]))
        location=file[0]

    def convertFile(self):
        
        save_url=self.location.text()
        
        if len(save_url)==0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Enter a valid location")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()

        else:
            originalImage = cv2.imread(location,0)
            new_im = Image.fromarray(originalImage)
            new_im.save(save_url+ "/op.png")
            self.image_2.setPixmap(QtGui.QPixmap(save_url+ "/op.png"))
            fname=""
            self.location.setText(fname)

            
            
            



    def browsefiles(self):
        option=QFileDialog.Options()
        widget=QWidget()
        fname= QFileDialog.getExistingDirectory(widget,"Select Directory")
        self.location.setText(fname)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
