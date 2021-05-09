xhost +
sudo docker run --rm -ti --net=host --ipc=host \
   -e DISPLAY=$DISPLAY \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   ivan1995arevalo/ping_my_image_09_04:latest
