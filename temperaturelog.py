"""
This program is a temperature log which takes measurements from the Raspberry Pi temperature sensor at given intervals.
The measurements will then be recorded in a file and actively graphed.
This program will run automatically when the Raspberry Pi is activated but it can be paused.
The date and time will also be calculated and included in the data.
The temperature is being recorded in degrees celcius.

Created by Cecelia Klein
October 15, 2019
"""
from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plot
import pygame
import time
import os, time

cpu = CPUTemperature()

#the temperature, date and time is recorded in a CSV file and actively graphed
plot.ion()
x = []
y = []

def write_tempcelcius(tempcelcius):
    with open("/home/pi/cpu_temperature_celcius.csv" , "a") as live_log:
        live_log.write("{0},{1}\n".format(strftime("%H:%M %Y-%m-%d"), str(tempcelcius)))

def graph(tempcelcius):
    x.append(time())
    y.append(tempcelcius)
    plot.clf()
    plot.scatter(x,y)
    plot.plot(x,y)
    plot.draw()

while True:
    tempcelcius = cpu.temperature
    write_tempcelcius(tempcelcius)
#   graph(tempcelcius)
    plot.pause(2)

#CSV can be found in the Desktop, open it to see the temperature live_log
#It takes a moment for the info to load into the CSV!
#Please give the program a moment to run before opening the CSV.
@reboot python3 /home/pi/Desktop/temperaturelog.py
