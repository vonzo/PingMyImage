# -*- coding: utf-8 -*-
"""
Created on Mon Apr  18 20:04:24 2021
@author: Ivan Arevalo

This program is capable of displaying the camera
stream and writting on the image the ping in ms
from  OTIV's web site.

Entrance point of the program.
"""
import concurrent.futures
import ImageProducer as ipcv
import PingRequester as pr
import queue

if __name__ == "__main__":
    # Declare ImageProducer instance
    image_producer = ipcv.ImageProducer()

    # Declare PingRequester instance
    ping_requester = pr.PingRequester()

    # Queue continer for ping values
    global_ping = queue.Queue()

    # Config/Launch threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        ping_thread = executor.submit(ping_requester.loop_ping, global_ping)
        camera_thread = executor.submit(image_producer.launch_webcam,
                                        global_ping)
        # Camera thread stops ping thread when stopped
        if(not camera_thread.result()):
            ping_requester.ask_to_stop()
