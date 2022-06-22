# friendly_watcher

Friendly Watcher is an app that allows you to share any window of any desktop application, as well as your own webcam.

To send video streams remotely, it is necessary to use a VPN or Multicast server to manage the streams.

On this occasion we will use a free VPN that provides a decentralized network, ZeroTier.

NOTE: This is a beta version of the app, and this program has been developed and used on linux only. 

### How it works? ###

* Encodes the image in h265 using CPU.
* HW compression will soon be added using "nvenc" for Nvidia graphics and "vaapih265enc" for Intel GPUs.
* In the case of webcam, it takes the already compressed stream and sends it.
* For the management and creation of pipelines, the Gstreamer framework is used. 
* It uses the Real Time Streaming Protocol (RTSP), which is an application-level network communication system that transfers real-time data from multimedia to an endpoint device.
* In the near future, will be available the option to use SRT (Secure Reliable Transport), which is an open source video streaming protocol that brings pristine quality, low-latency live video over the public internet.
* To process and manipulate the images, OpenCV (Open Source Computer Vision Library) is used, which is an open source computer vision and machine learning software library.
* The gui is based on Qt, which is a cross-platform application development framework.
* The app is written in Python, which is a high-level, interpreted, object-oriented programming language.

### How do I get set up? ###

* Install [gst-rtsp-launch](https://github.com/sfalexrog/gst-rtsp-launch) on your computer.
* To install the VPN, you need to install the [ZeroTier One](https://www.zerotier.com/download) client, and connect to the preconfigured network that is provided by the VPN.
* To change the configuration of the VPN, you need to go to the [ZeroTier One](https://www.zerotier.com/download) client, and go to the "Network" tab.
* Before proceeding with the execution of the installation script, change the configuration of the application, you need edit the file "config_friendly_watcher.py" in the folder "config". The configuration is done by editing the variables in the file.
* Install dependencies and python packages:
        
        > $ cd data
        > $ sudo /bin/bash install.sh


### How to use it? ###

First, you need to start the application:

        > $ cd utils
        > $ python3 friendly_watcher.py

In the Sender tab, you can choose between webcam or screen video input, by choosing one of them and pressing the Start button.
* In the case of selecting "Screen", the mouse will turn into a crosshair with which you have to click on the window you want to share.
* In the case of selecting "Webcam", will use the default webcam.

Once the stream is initialized, the status will be set to "Running!" and the Ip address with the position and endpoint of the stream will appear in "Your stream dir:".

On the other hand, to consume the stream, go to the "Watcher" tab, enter in "Streaming dir" the address that your friend has given you and press the Start button.

Finally, from the Watcher tab, you can take snapshots of the flow you are consuming by clicking on the "Take Snapshot" button.

### Video and screenshots examples ###

You can see the video and the screenshots in the folder "resources". 

By the other hand, you can acces to watch the video on YouTube clicking on the next icon.

<p>
        <p align="center">
        <a href="https://www.youtube.com/watch?v=2YbCavNb07A">
        <img src="data/icons/screen-svgrepo-com.svg" width="100" height="100">
</p>

## Run on docker
This intends to automatize the process of building, running, starting and stopping docker images/containers. 

First, you need to install the docker:

        > $ cd data
        > $ sudo /bin/bash install.sh docker

### Usage

* The *Dockerfile* starts from a official ubuntu image, installs terminator and configures a little bit the *.bashrc* in order to be coloured and initialize ubuntu. 


* The *run_docker.sh* script contain all the required options to run the docker image with the same network as the host, with GUIs enabled, the dbus shared with the host, ...  . The scripts takes 2 optional arguments (container name and image name) in order to easily create new containers/images with the new changes.


        ./run_docker.sh  <new_container_name> <new_image_name>      
                        
                     # Default img_name = 'docker_friendly_watcher'
                     # Default continer_name = 'friendly_watcher'
                    

### **Compiles Dockerfile; if the named container already exists, starts it; else it runs the compiled image**.

### Run fiendly_watcher app on docker
Is the same as running the application from the command line in the system.
First, you need to install the application:

        > $ cd friendly_watcher/data
        > $ sudo /bin/bash install.sh

Finally, you can run the application:

        > $ cd friendly_watcher/utils
        > $ python3 friendly_watcher.py

**!!!!** If you modify the Dockerfile but you don't remove the container, it will start previous container, not a new one with the new image. To do so:

    $ docker container rm docker_friendly_watcher && ./run_docker.sh

### Special thanks to: ###

[Fidel Gonzalez](https://github.com/lotape6) for the support of docker integration.

### Contribution guidelines ###

* [Gstreamer](https://gstreamer.freedesktop.org/)
* [Python](https://www.python.org/)
* [QT](https://www.qt.io/)
* [OpenCV](https://opencv.org/)
* [ZeroTier One](https://www.zerotier.com/download)
* [SRT](https://github.com/Haivision/srt)
* [Gst-rtsp-launch](https://github.com/sfalexrog/gst-rtsp-launch)
* [Docker](https://www.docker.com/)


### Who do I talk to? ###

* [Mouhsine Kassimi](mouhsine98@gmail.com)
