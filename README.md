# Ping my Image
This program gets the video stream from your camera and meassures the ping of your computer to https://www.otiv.ai/ and writes it over the image and displays it

## Requirements
1. You should have acces to `sudo`
2. `pip`
3. python (3.8 is recommended)
4. ffmpeg libsm6 libxext6 can be intalled with `apt-get install ffmpeg libsm6 libxext6  -y`
5. opencv-python
6. pythonping

### pythonping
pythonping *needs* superuser privileges to be able to get the ping. It is important to make sure that your python installation user matched with `sudo`

All the required libraries can be installed running the `sudo install_dependencies.sh`, or directly calling `sudo pip` and the requirements.txt file.

## Launch
I can't stress enough how necessary it is to have superuser privileges when running this program. You can run it with:
```
sudo python ping_my_image.py
```

just make sure the python you launch is the same where system's `pip` points to.

## Behaviour
When you launch the program there are two options: 

1. Your camera is recognized, then the video stream will be shown with the respective ping on it

![ImageOfCameraStream](SampleImages/example1.png)

2. Your camera is not recognized, then a random image will be generated every half a second with the ping written on top.

![ImageOfRandomStream](SampleImages/example2.png)

### The ping will be set to `-1` in case of not having the rigth permissions or lossing internet connection
## Stop program 
To stop the program just hit the 'q' button (make sure no caps lock) 

## Docker Image
### Drawbacks
This software was developed in a Windows Machine and I managed to test it using an ubuntu VM, because of this I couldn't test the camera in Docker, I think it is posible to use (not on Docker+Windows!) but I couldn't test it. So when running the Docker image you will *always* get the random image version.

### Pull from Docker hub 
Just run:
```
sudo docker pull ivan1995arevalo/ping_my_image_09_04
```

### Launch
To launch the container and have acces to the displayed images you should run the script (if you got the Git repo):
```
./launchContainer.sh
```
If you don't have this file just run:
```
xhost +
sudo docker run --rm -ti --net=host --ipc=host \
   -e DISPLAY=$DISPLAY \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   ivan1995arevalo/ping_my_image_09_04:latest
```
