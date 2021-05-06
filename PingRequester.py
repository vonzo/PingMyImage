# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:12:41 2021

@author: Ivan Arevalo
"""
import time

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
            time.sleep(1.0)
            global_ping[0] = self.ping_otiv()
            self.count += 1
