import wave, numpy, struct, random
def distorter(distortionRate):
    # Open
    w = wave.open("running.wav", "rb")
    p = w.getparams()
    print p
    frames = p[3]  # number of frames
    s = w.readframes(frames)
    w.close()
    length = p[3] /2
    print length
    distortionRate = float(distortionRate)

    # Edit
    s = numpy.fromstring(s, numpy.int16) # half amplitude
    for i in range(0,length):
        s[i] = s[i] * distortionRate
    s = struct.pack('h' * len(s), *s)
    # Save
    w = wave.open("outputDistorted.wav", "wb")
    w.setparams(p)
    w.writeframes(s)
    w.close()

    print "Finished."


def randomToneGenerator():
    w = wave.open("running.wav","rb")
    p = w.getparams()
    frames = p[3]
    length = frames / 2
    s = w.readframes(frames)
    toneSectionNumber = 3
    w.close()

    s = numpy.fromstring(s, numpy.int16)
    pointer = 0
    for i in range(0,toneSectionNumber):
        randomNumber = random.randrange(0, 441100)
        for i in range(0,length/toneSectionNumber):
            s[pointer] = randomNumber
            pointer += 1
    s = struct.pack('h' * len(s), *s)

    w = wave.open("outputRandom.wav","wb")
    w.setparams(p)
    w.writeframes(s)
    w.close()
    print "Done."

def smoothTone():
    w = wave.open("running.wav","rb")
    p = w.getparams()
    frames = p[3]
    length = frames / 2
    s = w.readframes(frames)
    toneSectionNumber = 5
    w.close()

    s = numpy.fromstring(s, numpy.int16)
    increase = True

    for i in range(0,length):
        if increase == True:
            s[i] = i * toneSectionNumber
            if (i*toneSectionNumber) >= frames / toneSectionNumber:
                increase = False
        else:
            s[i] = i * - 3
            if (i * toneSectionNumber) >= frames / toneSectionNumber:
                increase = True


    s = struct.pack('h' * len(s), *s)
    w = wave.open("outputSmooth.wav","wb")
    w.setparams(p)
    w.writeframes(s)
    w.close()
    print("Over.")






#distortionRate = raw_input("Input a number for distortion: ")
#distorter(distortionRate)

#randomToneGenerator()

smoothTone()