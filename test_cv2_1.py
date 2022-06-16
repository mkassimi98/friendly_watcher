from locale import windows_locale
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        self.StartFeedButton = QPushButton("Start Feed")
        self.StartFeedButton.clicked.connect(self.StartFeed)
        self.VBL.addWidget(self.StartFeedButton)
        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)
        self.Entry_dir = QLineEdit()
        self.VBL.addWidget(self.Entry_dir)

        self.setWindowTitle("Friendly Watcher")
        self.setGeometry(300, 300, 300, 300)
        

        self.Qtext = QTextEdit()
        self.Qtext.setText("Hello World")
        
        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
    
    def StartFeed(self):
        self.Worker1.start()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            try:
                ret, frame = Capture.read()
                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image, 1)
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(1280, 720, Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
                    self.ImageUpdate.emit(Pic)

            except:
                pass
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    try:
        App = QApplication(sys.argv)
        Root = MainWindow()
        Root.show()
        sys.exit(App.exec())
    except Exception as e:
        print(e)