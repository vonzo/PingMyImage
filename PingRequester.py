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
        self.__ping = -1
        # When this variable changes, the thread is asked to stop
        self.__keepAlive = False
        # Remembers if Error mesage was written to avoid repetition
        self.__printError = True

    # Ping OTIV, the URL is hard-coded, but of course it could be a parameter
    # Return ping in ms
    def ping_otiv(self):
        temp_ping_ms = -1.0
        try:
            response_list = ping('www.otiv.ai', timeout=1)
            temp_ping_ms = response_list.rtt_avg_ms
            self.__printError = True
        except:
            if(self.__printError):
                print("Network problem")
                self.__printError = False
        return temp_ping_ms

    # Ask thread to stop (non blocking)
    def ask_to_stop(self):
        self.__keepAlive = False

    # Get ping from OTIV every second Thread Function
    # global_ping: Queue Object where the ping should be contianed
    def loop_ping(self, global_ping):
        self.__keepAlive = True
        while(self.__keepAlive):
            self.__ping = self.ping_otiv()
            global_ping.put(self.__ping)
            time.sleep(1.0)
