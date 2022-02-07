import sys

import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5 import uic

form_window = uic.loadUiType('./mainwidget.ui')[0]

class Exam(QWidget, form_window):
    Circle = 0
    Rectangle = 1
    Ellipse = 2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paintcolor = (50, 200, 50)
        self.brush = 2
        self.start_pos = None
        self.figure = Exam.Circle
        self.img = np.full((500, 500, 3), 255, dtype=np.uint8)
        qImg = QtGui.QImage(self.img, 500, 500, 500 * 3, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)
        self.cmb_figure.currentIndexChanged.connect(self.setFigure)
        self.btn_red.clicked.connect(self.setColor)
        self.btn_blue.clicked.connect(self.setColor)
        self.btn_green.clicked.connect(self.setColor)
        self.btn_colorpick.clicked.connect(self.user_color)
        self.sb_thickness.valueChanged.connect(self.user_brush)

    def user_brush(self, thick):
        self.brush = thick

    def user_color(self):
        p_color = QColorDialog.getColor()
        self.paintcolor = (p_color.red(), p_color.green(), p_color.blue())

    def setColor(self):
        btn_name = self.sender().objectName()
        if btn_name == 'btn_red':
            self.paintcolor = (200, 50, 50)
        elif btn_name == 'btn_blue':
            self.paintcolor = (50, 50, 200)
        elif btn_name == 'btn_green':
            self.paintcolor = (50, 200, 50)

    def setFigure(self):
        figure = self.cmb_figure.currentText()
        if figure == 'Circle':
            self.figure = Exam.Circle
        elif figure == 'Rectangle':
            self.figure = Exam.Rectangle
        elif figure == 'Ellipse':
            self.figure = Exam.Ellipse


    def img_to_label(self, src):
        h, w, c = src.shape
        qImg = QtGui.QImage(src, w, h, w * c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.start_pos = (event.x(), event.y())
    def mouseMoveEvent(self, event):
        if isinstance(self.start_pos, tuple):
            new_img = self.img.copy()
            if self.figure == Exam.Circle:
                cv2.circle(new_img, self.start_pos,
                           int(((self.start_pos[0] - event.x()) ** 2 + (self.start_pos[1] - event.y()) ** 2) ** 0.5),
                           self.paintcolor, self.brush)
            elif self.figure == Exam.Rectangle:
                cv2.rectangle(new_img, self.start_pos,
                              (event.x(), event.y()),
                              self.paintcolor, self.brush)
            elif self.figure == Exam.Ellipse:
                cv2.ellipse(new_img,
                            (self.start_pos,
                            (abs(self.start_pos[0] - event.x())*2,
                             abs(self.start_pos[1] - event.y())*2), 0),
                            self.paintcolor, self.brush)
            self.img_to_label(new_img)
    def mouseReleaseEvent(self, event):
        if self.figure == Exam.Circle:
            cv2.circle(self.img, self.start_pos,
                       int(((self.start_pos[0] - event.x()) ** 2 + (self.start_pos[1] - event.y()) ** 2) ** 0.5),
                       self.paintcolor, self.brush)
        elif self.figure == Exam.Rectangle:
            cv2.rectangle(self.img, self.start_pos,
                          (event.x(), event.y()),
                          self.paintcolor, self.brush)
        elif self.figure == Exam.Ellipse:
            cv2.ellipse(self.img,
                        (self.start_pos,
                         (abs(self.start_pos[0] - event.x())*2,
                          abs(self.start_pos[1] - event.y())*2), 0),
                    self.paintcolor, self.brush)
        self.img_to_label(self.img)
        self.start_pos = None
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())