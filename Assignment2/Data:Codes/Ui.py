#Author: Hyunjae Kim
#Date: 06/23/2022
from PIL import Image
from random import seed
from random import randint

import os
import sys
import string
import time

while True:
	press = input("Press 1 to open the image or Press 2 to exit: ")

	pf = open('prng-service.txt','r+')
	ifile = open('image-service.txt','r+')
	pf.truncate(0)
	ifile.truncate(0)
	pf.close()
	ifile.close()
	
	if(press == "1"):
		f = open('prng-service.txt', 'a')
		time.sleep(1)
		f.write("run")
		f.close()
		time.sleep(5)
		f1 = open('prng-service.txt','r+')
		text = f1.readline()
		words = text.split()
		f2 = open('image-service.txt', 'r+')
		f3 = open('image-service.txt', 'a')
		f2.truncate(0)
		f3.write(words[0])
		f2.close()
		f3.close()
		time.sleep(10)
		f4 = open('image-service.txt','r+')
		file_path = f4.read()
		print(file_path)
		im = Image.open(file_path, mode = 'r')
		im.show()	
		f4.close()
		f1.close()
	elif(press == "2"):
		break
	else:
		print("Unknown Option") 

