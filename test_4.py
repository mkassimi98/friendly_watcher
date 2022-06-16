import sys
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import GObject, Gst, GstVideo
from PyQt5.QtWidgets import *

Gst.init(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.pipeline = Gst.parse_launch(
            'videotestsrc name=source ! videoconvert name = convert ! xvimagesink name=sink')  # xvimagesink, ximagesink
        self.source = self.pipeline.get_by_name("source")
        self.videoconvert = self.pipeline.get_by_name("convert")
        self.sink = self.pipeline.get_by_name("sink")

        self.display = QWidget()

        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle("Prova_gst_qt5")

        self.windowId = self.winId()

    def setup_pipeline(self):

        self.state = Gst.State.NULL
        self.source.set_property('pattern', 0)

        if not self.pipeline or not self.source or not self.videoconvert or not self.sink:
            print("ERROR: Not all elements could be created")
            sys.exit(1)

        # instruct the bus to emit signals for each received message
        # and connect to the interesting signals
        bus = self.pipeline.get_bus()

        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect('sync-message::element', self.on_sync_message)

    def on_sync_message(self, bus, msg):
        if msg.get_structure().get_name() == 'prepare-window-handle':
            msg.src.set_window_handle(self.windowId)

    def start_pipeline(self):
        self.pipeline.set_state(Gst.State.PLAYING)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setup_pipeline()
    window.start_pipeline()
    window.show()
    sys.exit(app.exec_())
