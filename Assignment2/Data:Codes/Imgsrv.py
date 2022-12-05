#Author: Hyunjae Kim
#Date: 06/23/2022

from ast import Mod
from operator import mod
import os
import sys
import string
import time
import math

while True:
    time.sleep(1)
    f = open('image-service.txt', 'r+')
    text = f.readline()
    words = text.split()
    if(len(words) == 0): continue
    if(words[0].isdigit() == True):
        v = int(words[0])
        v = v % 4
        time.sleep(3)
        f.truncate(0)
        f.close()
        f2 = open('image-service.txt', 'a')
        f2.write("/Users/hyunjaekim/Desktop/CS361-A2/")
        f2.write(str(v))  
        f2.write(".jpg")
        f2.close()