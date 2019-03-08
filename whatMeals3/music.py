# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:03:54 2019

@author: C-82
"""

from ctypes import windll, c_buffer
import random
import tkinter
import threading
import os
import psutil
import signal
from multiprocessing import Process

class music:
    def __init__(self): 
        self.p = Process()
        self.cnt = 0
        self.lis = ['C://Users//C-82//Music//a.mp3','C://Users//C-82//Music//b.mp3','C://Users//C-82//Music//c.mp3',
        'C://Users//C-82//Music//d.mp3','C://Users//C-82//Music//e.mp3','C://Users//C-82//Music//f.mp3']
    def process_play(self):
        filename = self.lis[self.cnt]
        w32mci = windll.winmm.mciSendStringA
        _alias = 'mp3_%s' % (str(random.random()))
        buffer = c_buffer(255)
        w32mci(str('open "%s" alias %s' % (filename,_alias)).encode(), buffer, 254, 0)
        w32mci(str('set %s time format milliseconds' % _alias).encode(), buffer, 254, 0)
        w32mci(str('status %s length' % _alias).encode(), buffer, 254, 0)
        leng = int(buffer.value)
        start = 0
        end = leng
        w32mci(str('play %s from %d to %d' % (_alias, start, end)).encode(), buffer, 254, 0)
        import time
        time.sleep(1000)
        w32mci(str('stop %s' % _alias).encode(), buffer, 254, 0)

    def play(self):
        if self.p.is_alive() == True:
            self.p.terminate()
        self.cnt = (self.cnt + 1) % 6
        self.p = Process(target = self.process_play,daemon = True)
        self.p.start()
    def close(self):
        if self.p.is_alive() == True:
            self.p.terminate()