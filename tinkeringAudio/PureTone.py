from wave import *
import struct
import math
import winsound

values = []
SAMPLE_LENGTH = 44100*8
FREQUENCY = 560
SAMPLE_RATE = float(44100)
VOLUME = 1
BIT_DEPTH = 32767
CHANNELS = 2
timer = 0
noise_out = open("unknownNoise.wav", "w")
noise_out.setparams((CHANNELS, 2, SAMPLE_RATE, SAMPLE_LENGTH, 'NONE', 'not compressed'))

for i in range(0, SAMPLE_LENGTH):
    value = math.sin(2.0 * math.pi*FREQUENCY*( i / SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
    packaged_value = struct.pack('h', value)

    noise_out.writeframes(packaged_value)
noise_out.close()