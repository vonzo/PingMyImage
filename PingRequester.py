# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:12:41 2021

@author: Ivan Arevalo
"""
import time
import queue

class PingRequester:
    def __init__(self):
        self.ping = 0
        self.count = 0
        self.keepAlive = True
      
    def ping_otiv(self):
        from pythonping import ping
        response_list = ping('www.otiv.ai', size=40, count=10)
        return response_list.rtt_avg_ms
        
    def ask_to_stop(self):
        self.keepAlive = False
    
    def loop_ping(self, global_ping):
        while(self.keepAlive):
            temp_var = self.ping_otiv()
            global_ping.put(temp_var)
            time.sleep(1.0)
            self.count += 1
