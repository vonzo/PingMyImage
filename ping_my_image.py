# -*- coding: utf-8 -*-
"""
Created on Mon Apr  18 20:04:24 2021

@author: Ivan Arevalo
"""
import concurrent.futures
import ImageProducer as ipcv
import PingRequester as pr
import time 

    
if __name__ == "__main__":
    #Declare ImageProducer instance
    image_producer = ipcv.ImageProducer(False)
    #Declare PingRequester instance
    ping_requester = pr.PingRequester()
    
    global_ping = [0]
    
    # #Config threads 
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        ping_thread   = executor.submit(ping_requester.loop_ping, global_ping)
        camera_thread = executor.submit(image_producer.launch_webcam, global_ping)
        if(not camera_thread.result()):
            ping_requester.ask_to_stop()
        ping_value    = ping_thread.result()

    
    


    

