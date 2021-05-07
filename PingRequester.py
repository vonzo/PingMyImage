# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:12:41 2021
@author: Ivan Arevalo

Class PingRequester: This class is capable of getting the 
                     ping in milisecond form www.otiv.ai
                     and do it in a loop every 1.0 seconds.
"""
import time
from pythonping import ping

class PingRequester:
    def __init__(self):
        # Store ping value in ms here
        self.__ping = 0
        # When this variable changes, the thread is asked to stop
        self.__keepAlive = False
      
    # Ping OTIV website, the URL is hard-coded, but of course it could be a parameter
    # Return ping in ms
    def ping_otiv(self):
        response_list = ping('www.otiv.ai', size=40, count=10)
        return response_list.rtt_avg_ms
        
    # Ask thread to stop (non blocking) 
    def ask_to_stop(self):
        self.__keepAlive = False
    
    # Get ping from OTIV every second Thread Function
    # global_ping : Queue Object where the ping should be contianed
    def loop_ping(self, global_ping):
        self.__keepAlive = True
        while(self.__keepAlive):
            self.__ping = self.ping_otiv()
            global_ping.put(self.__ping)
            time.sleep(1.0)
