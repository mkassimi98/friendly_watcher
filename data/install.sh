#!/bin/bash

dependencies=(git python3 python3-pip python3-venv python3-setuptools libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio)

# Install dependencies
function dependencies_install() {
    echo "Installing dependencies..."
    sudo apt-get update
    echo 'Installing Git and Python...'
    for i in "${dependencies[@]}"; 
    do
        sudo apt-get install -y "$i"
    done
    echo 'Installing python packages...'
    # Check if python requirements.txt are available
    if [ ! -f requirements.txt ]; then
        echo 'requirements.txt not found'
        exit 1
    fi
    pip3 install --user -r requirements.txt
}

# Install config file
function config_install() {
    echo "Installing config file..."
    sudo cp config_friendly_watcher.py /usr/lib/python3/dist-packages/
}

dependencies_install
config_install