"""
Migracion del codigo del enlace siguiente a PyQt6
https://medium.com/@ilias.info.tel/display-opencv-camera-on-a-pyqt-app-4465398546f7

"""
import sys
import numpy as np

from PyQt6.QtCore import QObject, QThread,  Qt, QTime
from PyQt6.QtCore import pyqtSignal as Signal
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider
from PyQt6.QtWidgets import QMainWindow
import sys

from PyQt6.QtWidgets import (QWidget, QPushButton,
        QHBoxLayout, QVBoxLayout, QApplication)

from PyQt6.QtGui import QImage
from PyQt6.QtGui import QImage, QPixmap

from ast import literal_eval as make_tuple
import os
from PyQt6.QtCore import QSize, Qt, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QPushButton,
        QHBoxLayout, QVBoxLayout, QApplication)
import imutils
import cv2
import random

from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout

class MyThread(QThread):

    frame_signal = Signal(QImage)



    def run(self):
        self.opcion = -1
        self.umbral = 128
        self.Lista = []
        
        self.cap = cv2.VideoCapture(0)
        #self.cap = cv2.VideoCapture(2) # no funciona para una SEGUNDA CAMARA conectada a la Laptop

        while self.cap.isOpened():
            _,frame = self.cap.read()
            #print (frame.shape)
            frame = self.cvimage_to_label(frame)
            self.frame_signal.emit(frame)
    
    def cvimage_to_label(self,image):
        
        # Forza a redimensionar la imagen
        image = imutils.resize(image,width = 640)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        #print (image.shape)

        # Introducir el procesamiento de OpenCV
        for e in self.Lista:
            image = cv2.circle(image, e, 5, (255,0,255), 5)

        if self.opcion==1:
            x=1 # NO HACER NADA
            #image = cv2.circle(image, (10,10), 100, (255,0,255), 5)

                
            
            #    print (e)
                     
        if self.opcion==2:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            ret,gray = cv2.threshold(gray,self.umbral,255,cv2.THRESH_BINARY)
            image = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        
        if self.opcion==3:
            #image = 255 - image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_blurred = cv2.blur(gray, (7, 7)) 
            detected_circles = cv2.HoughCircles(gray_blurred, 
				            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
			            param2 = 30, minRadius = 1, maxRadius = 40) 

            # Draw circles that are detected. 
            if detected_circles is not None: 
                detected_circles = np.uint16(np.around(detected_circles)) 

                for pt in detected_circles[0, :]: 
	                a, b, r = pt[0], pt[1], pt[2] 

	                # Draw the circumference of the circle. 
	                cv2.circle(image, (a, b), r, (0, 255, 0), 2) 


        image = QImage(image,
                       image.shape[1],
                       image.shape[0],
                       QImage.Format.Format_RGB888)
      


        return image

    def setLista (self, Lista):
        #print ("Dentro del Hilo de Tanga") 
        self.Lista = Lista[:]
        #for x in self.Lista:
        #    print ("XXXX",x)

class MiEtiqueta(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()      
        self.Lista=[]
        print ("Ancho-Alto:",self.height(),self.width()) 
        self.setStyleSheet("border: 1px solid black;")

    clicked = pyqtSignal()

    def mousePressEvent(self, e):
        self.x = e.position().x()
        self.y = e.position().y()
        self.Lista.append((int(self.x),int(self.y)) )
        #print (self.Lista)
        self.clicked.emit()


#class MainApp(QtWidgets.QMainWindow):
class MainApp(QWidget):

    def convertQImageToMat(self,incomingImage):
        '''  Converts a QImage into an opencv MAT format  '''
        incomingImage.save('temp.png', 'png')
        mat = cv2.imread('temp.png')
        return mat

    def update (self):
        # get the radio button the send the signal
        rb = self.sender()

        # check if the radio button is checked
        if rb.isChecked():
            if rb.text()=="A":
                self.camera_thread.opcion=1
            if rb.text()=="B":
                self.camera_thread.opcion=2
            if rb.text()=="C":
                self.camera_thread.opcion=3
            
                      
            #self.result_label.setText(f'You selected {rb.text()}')
        
    def Metodo (self):
        r=1
        self.camera_thread.setLista(self.label.Lista)
        for i in self.label.Lista:
            print("XX",i)
        
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.disable_enable_UI(False)

        self.show()
    
    def disable_enable_UI(self,Valor):
        self.ListaControlesHabilitar = [self.label, self.boton2, self.slider, self.rb_android, self.rb_windows, self.rb_ios]
        for i in self.ListaControlesHabilitar:
            i.setEnabled(Valor)

    def init_ui(self):
        self.setFixedSize(800,640)

        self.setWindowTitle("Camera FeedBack")

        
        #widget = QtWidgets.QWidget(self)

        #layout = QtWidgets.QVBoxLayout()
        #widget.setLayout(layout)

        #self.label = QtWidgets.QLabel()
        self.label = MiEtiqueta()
        self.label.clicked.connect(self.Metodo)
        
        #self.label.resize(640, 480)
        BUTTON_SIZE = QSize(640, 480)
        #self.label.setMinimumSize(BUTTON_SIZE)
        self.label.setFixedSize(BUTTON_SIZE)
        
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setScaledContents(True)
        #self.label.setFixedHeight(480)
        #layout.addWidget(self.label)

        self.open_btn = QtWidgets.QPushButton("Open The Camera", clicked=self.open_camera)
        #layout.addWidget(self.open_btn)

        self.boton2 = QtWidgets.QPushButton("Save frame")
        #layout.addWidget(self.boton2)

        self.camera_thread = MyThread()
        self.camera_thread.frame_signal.connect(self.setImage)

        self.boton2.clicked.connect(self.save_frame)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.open_btn)
        vbox.addWidget(self.boton2)

        vbox.addWidget(QLabel("Umbral"))
        
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.valueChanged.connect(self.display)
        self.slider.setTickInterval(8)
        self.slider.setValue(128)
        vbox.addWidget(self.slider)
        

        self.rb_android = QRadioButton('A', self)
        self.rb_android.setChecked(True)
        self.rb_android.toggled.connect(self.update)
        vbox.addWidget(self.rb_android)

        self.rb_ios = QRadioButton('B', self)
        self.rb_ios.toggled.connect(self.update)
        vbox.addWidget(self.rb_ios)

        self.rb_windows = QRadioButton('C', self)
        self.rb_windows.toggled.connect(self.update)
        vbox.addWidget(self.rb_windows)

        

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addLayout(vbox)
        
        self.setLayout(hbox)

    def display(self,value):
        self.camera_thread.umbral=value
        print(value)

    def open_camera(self):        
        self.camera_thread.start()
        print(self.camera_thread.isRunning())
        self.disable_enable_UI(True)


    def save_frame (self):
        OpenCVImg = self.convertQImageToMat (self.LastPixMap)
        cv2.imwrite("Temporalito.png",OpenCVImg )

        

    @Slot(QImage)
    def setImage(self,image):
        self.LastPixMap = QPixmap.fromImage(image)
        self.label.setPixmap(self.LastPixMap)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainApp()
    sys.exit(app.exec())
