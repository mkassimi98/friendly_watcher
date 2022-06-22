#!/bin/bash

dependencies=(git python3 python3-pip python3-venv python3-setuptools pyqt5-dev-tools pyqt5-dev ca-certificates curl gnupg lsb-release python3-opencv)

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
    echo "Installing video manager library..."
    sudo cp ../utils/video_manager/gst_manager.py /usr/lib/python3/dist-packages/
    sudo cp ../utils/video_manager/opencv_manipulate.py /usr/lib/python3/dist-packages/
}

# install Docker 
function docker_install() {
    echo "Installing Docker."
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

}


dependencies_install
config_install

if ["$1" == "docker"]; then
    docker_install
fi
