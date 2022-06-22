import os

# TODO: Add a way to get the video path from the user
# TODO: Add SRT implementation and optimize gstreamer using HW acceleration

class GST_Manager():
    def __init__(self, source):
        super().__init__()
        self.source = source
        
    def StartStream(self):
        if self.source == "Screen":
            try:
                # Select screen to stream
                self.output = os.popen("xwininfo | grep 'Window id'").read()
                self.win_id = self.output[21:30]
                os.system("gst-rtsp-launch -e Screen '( ximagesrc use-damage=0 startx=0 xid={} ! queue leaky=2 ! video/x-raw,framerate=60/1 ! videoconvert ! x265enc ! rtph265pay pt=96 name=pay0 )' > /dev/null 2>&1 &".format(self.win_id))
                # TODO: change it to gst return value
            except Exception as e:
                print("Error: " + str(e))

        else:
            try:
                # Stream camera feed
                os.system("gst-rtsp-launch -e Camera '( v4l2src device=/dev/video0 ! queue leaky=2 ! rtpjpegpay pt=96 name=pay0 )' > /dev/null 2>&1 &")
                # TODO: change it to gst return value
            except Exception as e:
                print("Error: " + str(e))
    
    def StopStream(self):
        try:
            os.system("pkill gst-rtsp-launch")
        except Exception as e:
            print("Error: " + str(e))
    
