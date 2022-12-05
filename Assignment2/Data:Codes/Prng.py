#Author: Hyunjae Kim
#Date: 06/23/2022

from random import seed
from random import randint

import os
import sys
import string
import time

while True:
    time.sleep(1)
    f = open('prng-service.txt', 'r+')
    f2 = open('prng-service.txt', 'a')
    text = f.read(3)
    time.sleep(1)
    if(text == "run"):
        value = randint(0,1000)
        f.truncate(0)
        time.sleep(1)
        f2.write(str(value))
    f.close()
    f2.close()

