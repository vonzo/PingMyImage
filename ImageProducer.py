# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:04:24 2021

@author: Ivan Arevalo
"""
import cv2
import numpy as np

class ImageProducer:
    def __init__(self, bContainer):
        self.bContainer = bContainer
        self.ping = 0
        self.keepAlive = True
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
    def launch_webcam(self, global_ping):
        if(not self.bContainer):
            cap = cv2.VideoCapture(0)
            while(self.keepAlive):
                # Capture frame-by-frame
                ret, frame = cap.read()
            
                cv2.putText(frame, str(global_ping[0])+"ms" ,(10,50), self.font, 1,(255,100,100),2)
                
                # Display the resulting frame
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.keepAlive = False
                    break
            
            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
        else:
            while(self.keepAlive):
                time.sleep(1)
                img=np.random.randint(0,255,size=[500,500,3],dtype=np.uint8)
                #Color range 0-255, size 256*256, three-channel color
                cv2.imshow("img",img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.keepAlive = False
                    break
        return self.keepAlive

