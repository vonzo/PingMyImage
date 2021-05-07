# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:04:24 2021

@author: Ivan Arevalo
"""
import cv2
import numpy as np
import time
import queue

class ImageProducer:
    def __init__(self):
        self.bCameraFound = False
        self.ping = -1.0
        self.keepAlive = True
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.count =  0
        self.cap = cv2.VideoCapture(0) 
        if self.cap is None or not self.cap.isOpened():
            self.bCameraFound = False
            print('Warning: unable to open video source')
        else:
            self.bCameraFound = True
        
        
    def launch_webcam(self, global_ping):
        if(self.bCameraFound):
            while(self.keepAlive):
                if(not global_ping.empty()):
                    self.ping = global_ping.get(block=False, timeout=None)
                # Capture frame-by-frame
                ret, frame = self.cap.read()
            
                cv2.putText(frame, str(self.ping)+"ms" ,(10,50), self.font, 1,(255,100,100),2)
                
                # Display the resulting frame
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.keepAlive = False
                    break
            
            # When everything done, release the capture
            self.cap.release()

        else:
            while((self.keepAlive)): # and (self.count < 200)):
                ping_ms = global_ping.get()
                self.count += 1
                time.sleep(0.1)
                img=np.random.randint(0,255,size=[100,150],dtype=np.uint8)
                #Color range 0-255, size 256*256, three-channel color
                cv2.putText(img, str(ping_ms)+"ms" ,(10,50), self.font, 1,(255,100,100),2)
                cv2.imshow("img",img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.keepAlive = False
                    break
            cv2.destroyAllWindows()
        return self.keepAlive

