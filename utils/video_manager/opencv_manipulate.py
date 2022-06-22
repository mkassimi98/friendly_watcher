from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import time
import config_friendly_watcher as cfg

class OpenCV_Manager(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def __init__(self, stream_dir_to_thread):
        super().__init__()
        self.stream_dir = stream_dir_to_thread
        
    def run(self):
        self.ThreadActive = True
        RTSP_URL = self.stream_dir
        Capture = cv2.VideoCapture(RTSP_URL)
        while self.ThreadActive:
            try:
                self.ret, self.frame = Capture.read()
                if self.ret:
                    Image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                    ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(1280, 720, Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
                    self.ImageUpdate.emit(Pic)
            except Exception as e:
                print(e)
            
    def stop(self):
        self.ThreadActive = False
        self.quit()
        
    # TODO: change storage dir to user defined    
    def take_snap(self):
        try:
            tm_taked = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            cv2.imwrite(cfg.IMG_PATH+'Frame'+str(tm_taked)+'.jpg', self.frame)
        except Exception as e:
            print("Error: " + str(e))