# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:12:41 2021

@author: Ivan Arevalo
"""
class PingRequester:
    def __init__(self):
        self.ping = 0
        
    def ping_otiv(self):
        from pythonping import ping
        response_list = ping('www.otiv.ai', size=40, count=10)
        print(response_list.rtt_avg_ms)
    
    def loop_ping(self):
        while(True):
            self.ping_otiv()
