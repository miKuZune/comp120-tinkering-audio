from wave import *
import struct
import numpy

values = []
frames = []
noise_in = open("DemoEcho.wav", "r")
noise_out = open("DemoEchoResult.wav", "w")
SAMPLE_LENGTH = noise_in.getnframes()
FREQUENCY = 560
SAMPLE_RATE = float(44100)
VOLUME = 1
BIT_DEPTH = 32767
CHANNELS = 2
timer = 0

parameters = noise_in.getparams()
noise_out.setparams(parameters)
frameParam = parameters[3]
frame = noise_in.readframes(frameParam)

frame = numpy.fromstring(frame, numpy.int16)
for i in range(0, SAMPLE_LENGTH):
    frame[i] = frame[i]
frame = struct.pack('h' * len(frame), *frame)
noise_out.writeframes(frame)
for i in range(44100, SAMPLE_LENGTH):
    frame[i] = frame[i]
frame = struct.pack('h' * len(frame), *frame)
noise_out.writeframes(frame)
noise_out.close()
