#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:41:52 2021

@author: benedictpark
"""
# Import py modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import random
import math
from scipy.stats import beta
from collections import namedtuple
import os
import shutil
import csv
import keyboard
import pyautogui

# Import audio-related py modules
import pyaudio
import struct
import sounddevice as sd

########################################################
## Audio formatting
########################################################
# Audio format details
CHUNK = 1024 * 4 # set chunk size (small length * number of these lengths to plot)
FORMAT = pyaudio.paInt16 # 16-bit?
CHANNELS = 1 # one channel (mono)
RATE = 44100 # rate of audio file

p = pyaudio.PyAudio()

# Stream details (from audio format details)
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = CHUNK)

########################################################
## Plot format
########################################################
plt.ion()
plt.style.use('ggplot')
fig, ax = plt.subplots()

x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(-255, 255)
ax.set_xlim(0, CHUNK /2)

########################################################
## Stream audio (from microphone) and output waves
########################################################
while True:
    data = stream.read(CHUNK, exception_on_overflow = False) # Stream audio data?
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype = 'b')[::2] + 127 # Actual data stored as array
    line.set_ydata(data_int) # Declare y value for the current x value
    fig.canvas.draw() # Draw the lines
    fig.canvas.flush_events()
    sd.wait()
















