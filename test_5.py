import sys, os
from blinker import Signal
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import GObject, Gst
# import GObject, pyGst
# pyGst.require('1.0')
# import Gst
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QAction, QFileDialog, QMessageBox
# from PyQt5.QtGui import QApplication, QMainWindow, QPushButton, QFileDialog


class MainWindow(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.setWindowTitle('Audio-Player')
         self.resize(120, 50)
         self.move(500, 500)
         self.button = QPushButton(self)
         self.button.setText('Start')
         self.button.setMinimumSize(90, 0)
         self.setCentralWidget(self.button)
         self.button.clicked.connect(self.start_stop)
        #  self.
        #  self.(self.button, Signal('clicked()'), self.start_stop)
        #  self.player = Gst.element_factory_make('playbin', 'player')
         try:
             # alsasink pulsesink osssink autoaudiosink
             device = Gst.parse_launch('alsasink')
         except GObject.GError:
             print ('Error: could not launch audio sink')
         else:
            #  self.player.set_property('audio-sink', device)
             self.bus = self.player.get_bus()
             self.bus.add_signal_watch()
             self.bus.connect('message', self.on_message)

     def start_stop(self):
         if self.button.text() == 'Start':
             filepath = QFileDialog.getOpenFileName(self, 'Choose File')
             if filepath:
                 self.button.setText('Stop')
                 self.player.set_property('uri', 'file://' + filepath)
                 self.player.set_state(Gst.STATE_PLAYING)
         else:
             self.player.set_state(Gst.STATE_NULL)
             self.button.setText('Start')

     def on_message(self, bus, message):
         t = message.type
         if t == Gst.MESSAGE_EOS:
             self.player.set_state(Gst.STATE_NULL)
             self.button.setText('Start')
         elif t == Gst.MESSAGE_ERROR:
             self.player.set_state(Gst.STATE_NULL)
             err, debug = message.parse_error()
             print ('Error: %s' % err, debug)
             self.button.setText('Start')


if __name__ == '__main__':

     GObject.threads_init()
     qApp = QApplication(sys.argv)
    #  qApp.setApplicationName('Audio-Player')
    #  qApp.setQuitOnLastWindowClosed(True)
    #  qApp.setStyle('fusion')
    #  qApp.setPalette(qApp.style().standardPalette())
    #  qApp.(qApp, Signal('lastWindowClosed()'), qApp, 'quit()')
     mainwindow = MainWindow()
     mainwindow.show()
     sys.exit(qApp.exec_())