#! /usr/bin/env bash

CONTAINER_NAME=${1:-"docker-friendly-watcher"}
DOCKER_IMG_NAME=${2:-"friendly-watcher"}

OPTS=""

# Avoid ros network problems
OPTS=$OPTS" --net=host"

# Avoid GUIs errors
OPTS=$OPTS" --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority --privileged"

# Share NVIDIA GPU
OPTS=$OPTS" --device /dev/nvidia0:/dev/nvidia0 --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm"

# Run detatched
OPTS=$OPTS" -d"

# Name your container
OPTS=$OPTS" --name $CONTAINER_NAME"

# DBus stuff 
OPTS=$OPTS" --volume /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket"

# More options at the end of the script

xhost + 

IMAGE_PREV_ID=$(docker inspect --format '{{.Id}}' $DOCKER_IMG_NAME ) 

docker build -t $DOCKER_IMG_NAME . && \

if [ $( docker ps -a --format '{{.Names}}' | grep $CONTAINER_NAME | wc -c) -eq 0 ] ; then
    echo -e "\033[1;32m$DOCKER_IMG_NAME image not found!  Running it with the name '$CONTAINER_NAME' \033[0m"
    docker run -ti $OPTS $DOCKER_IMG_NAME
else
    IMAGE_NEW_ID=$(docker inspect --format '{{.Id}}' $DOCKER_IMG_NAME ) 

    if [ "$IMAGE_NEW_ID" != "$IMAGE_PREV_ID" ] ; then
        echo -e "\033[1;33m$DOCKER_IMG_NAME image has changed, but a container with '$CONTAINER_NAME' already exist!\033[0m"
        read -p "Please insert a new container to run the new image or leave it empty to run existing container: " NEW_NAME
   
        if [ "$(echo $NEW_NAME | wc -m)" -eq 1 ] ; then
            echo -e "\033[1;32m$DOCKER_IMG_NAME image found but no new name provided! Starting previous container '$CONTAINER_NAME'\033[0m"
            docker start $CONTAINER_NAME
        else
            echo -e "\033[1;32m$DOCKER_IMG_NAME image found but new name provided! Running a new container with the name '$NEW_NAME'\033[0m"
            OPTS=$(echo $OPTS | sed "s/$CONTAINER_NAME/$NEW_NAME/")
            CONTAINER_NAME=$NEW_NAME
            docker run -ti $OPTS $DOCKER_IMG_NAME
        fi
    else
        echo -e "\033[1;32m$DOCKER_IMG_NAME image found and has not changed! Starting previous container '$CONTAINER_NAME'\033[0m"
        docker start $CONTAINER_NAME
    fi

fi

# Execute terminator
docker exec -ti $CONTAINER_NAME terminator

trap "docker stop $CONTAINER_NAME" INT
sleep infinity



#____________________________________________________________________________
#      I want to share a directory with the guest!!!
# (╯°□°）╯︵ ┻━┻
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                    Try ' -v /path/to/host/dir:/path/to/guest/dir'
#                                                        ┬─┬ ノ( ゜-゜ノ)  
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# (ʘ‿ʘ) 
#____________________________________________________________________________

#      I want to share a device with the guest!!!
# (╯°□°）╯︵ ┻━┻
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                    Try for example ' -d /dev/ttyUSB0:/dev/ttyUSB0'
#                                                        ┬─┬ ノ( ゜-゜ノ)  
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# (◠﹏◠)
#____________________________________________________________________________

#      I want to forward an environment variable to the guest!!!
# (╯°□°）╯︵ ┻━┻
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                    Ensure the variable is set and try  ' -e VAR_NAME'
#                                                        ┬─┬ ノ( ゜-゜ノ)  
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# \(ᵔᵕᵔ)/ 
#____________________________________________________________________________