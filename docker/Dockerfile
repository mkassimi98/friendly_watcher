# https://hub.docker.com/ubuntu
FROM ubuntu:18.04

USER root

RUN apt-get update && apt-get -y --no-install-recommends install \
    sudo \
    vim \
    wget \
    build-essential \
    pkg-config \
    python3.6 \
    python3-pip \
    python3.6-dev \
    python3.6-venv \
    python-dev \
    python3-dev

    
RUN apt-get -y --no-install-recommends install \
    git \
    autoconf \
    automake \
    libtool \
    gstreamer-1.0 \
    gstreamer1.0-dev \
    libgstreamer1.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-doc \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 \
    gstreamer1.0-pulseaudio \
    python-gst-1.0 \
    libgirepository1.0-dev \
    libcairo2-dev \
    gir1.2-gstreamer-1.0 \
    python3-gi \
    python-gi-dev
# Clone the conf files into the docker container
RUN git clone https://github.com/mkassimi98/friendly_watcher.git

# TODO: uncomment when done
# RUN rm -rf /var/lib/apt/lists/*

# Copy Terminator Configuration file
RUN mkdir -p /root/.config/terminator/
COPY config/terminator_config /root/.config/terminator/config

# TODO: uncomment when done
# Install friendly_watcher
# RUN cd /home/friendly_watcher/data && /bin/bash/install.sh

# Run friendly_watcher program
# CMD ["python3", "/home/friendly_watcher/data/friendly_watcher.py"]


