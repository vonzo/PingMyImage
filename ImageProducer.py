# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:04:24 2021
@author: Ivan Arevalo

Class ImageProducer: This class is capable of getting the 
                     Image srtameing from the first camera
                     detected in the system.
                     This image will be displayed and the 
                     ping received will be written on it.
"""
import cv2
import numpy as np
import time

class ImageProducer:
    def __init__(self):
        # True if camera present
        self.bCameraFound = False
        # Alocate ping value here
        self.ping = -1.0
        # Keep alive thread
        self.keepAlive = True
        # Font for ping text on image
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        # Capture Object
        self.cap = cv2.VideoCapture(0) 
        #Check if camera is available
        if self.cap is None  or not self.cap.isOpened():
            self.bCameraFound = False
            print('Warning: unable to open video source, creating random image')
        else:
            self.bCameraFound = True
        
    # Image read and display Thread Function
    # global_ping : Queue Object where the ping should be contianed
    def launch_webcam(self, global_ping):
        if(self.bCameraFound):
            while(self.keepAlive):
                # Verify if queue is not empty
                if(not global_ping.empty()):
                    self.ping = global_ping.get(block=False, timeout=None)
      
                
                # Capture frame
                ret, frame = self.cap.read() # OpenCV's read() function doesn't throw exceptions
            
                if(ret):
                    # Write ping text on image
                    cv2.putText(frame, str(self.ping)+"ms" ,(10,50), self.font, 1,(255,100,100),2)
                
                    # Display the resulting frame
                    cv2.imshow('Camera Frame',frame)
                else:
                    print("Error: something went wrong, camera lost")
                    break
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.keepAlive = False
                    break
            
            # When everything done, release the capture
            self.cap.release()

        else:
            while((self.keepAlive)):
                # Verify if queue is not empty
                if(not global_ping.empty()):
                    self.ping = global_ping.get(block=False, timeout=None)
                    
                # Create random image every 0.5 seconds
                time.sleep(0.5)
                frame=np.random.randint(0,255,size=[100,150],dtype=np.uint8)
                
                # Write ping text on image
                cv2.putText(frame, str(self.ping)+"ms" ,(10,50), self.font, 1,(255,100,100),2)
                
                # Display the resulting frame
                cv2.imshow("Random Image",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.keepAlive = False
                    break
            # Destroy windows in any case
            cv2.destroyAllWindows()
        return self.keepAlive

