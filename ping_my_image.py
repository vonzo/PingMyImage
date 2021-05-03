# -*- coding: utf-8 -*-
"""
Created on Mon Apr  18 20:04:24 2021

@author: Ivan Arevalo
"""

import numpy as np
import threading
import ImageProducer as ipcv
import PingRequester as pr
    
if __name__ == "__main__":
    image_producer = ipcv.ImageProducer(True)
    ping_requester = pr.PingRequester()
    
    camera_thread = threading.Thread(target=image_producer.launch_webcam)
    camera_thread.start()
    
    ping_thread = threading.Thread(target=ping_requester.loop_ping())
    ping_thread.start()
    
    


    

