#!/usr/bin/env python
#coding: utf-8

'''
 Simulation 2017-I
 2. Random
 * Name: Viviana Márquez. 
 * Date: Saturday, February 11th, 2016
'''

import time

print ("This program will generate a 'random' number between 0 and 9...")
time.sleep(3)
print ("Please be patient...")

millis1 = int(round(time.time() * 1000))
#print (millis1)
print("*******")

lastdigit_millis1 = int(repr(millis1)[-1])
#print(lastdigit_millis1)
print("*")
#This number will generate a pause in the system in order to capture a new millisecond.

time.sleep(lastdigit_millis1)

millis2 = int(round(time.time() * 1000))
#print (millis2)
print("*******")

lastdigit_millis2 = int(repr(millis2)[-1])
#print(lastdigit_millis2)
print("*")
#This number will be the modulus. 

while (lastdigit_millis2==0): #To avoid dividing by zero
	time.sleep(lastdigit_millis1)
	millis2 = int(round(time.time() * 1000))
	lastdigit_millis2 = int(repr(millis2)[-1])
	print("*-*-*")

random = millis1 % lastdigit_millis2

print("The random number generated is: "+str(random))
