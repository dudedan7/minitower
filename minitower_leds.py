import board 
import neopixel
import time 
from random import randint

# D18 means GPIO18, 4 LEDs
pixels    = neopixel.NeoPixel(board.D18, 4)
pixels[0] = (0,0,0) # oled board LED
pixels[1] = (0,0,0) # fan LED 1
pixels[2] = (0,0,0) # fan LED 2 
pixels[3] = (0,0,0) # fan LED 3

# set a constant for loop length, determines shifting speed of colors
loopTime = 255*4

#dictionary of colors to shift through
colorDict = {
#'lightBlueSky' : 0x6ECBF6,
#'mediumOrchid' : 0xC252E1,
#'lavender'     : 0xE0D9F6,
#'royalBlue'    : 0x586AE2,
#'midnightBlue' : 0x2A2356
'neon1':0x020315,
'neon2':0xE033E7,
'neon3':0x5932E5,
'neon4':0xB332E5,
'neon5':0x8633E7
}

colorRGBTuples = []
for color in colorDict.keys():
    colorHex = colorDict[color]
    colorR   = ((colorHex & 0xFF0000) >> 16)
    colorG   = ((colorHex & 0x00FF00) >> 8)
    colorB   =  (colorHex & 0x0000FF)
    colorRGB = (colorR,colorG,colorB)
    colorRGBTuples.append(colorRGB)

#set color shifts for easy looping
colorShifts = []
for i in range(0, len(colorRGBTuples)):
    if i != (len(colorRGBTuples)-1):
        colorShifts.append([colorRGBTuples[i], colorRGBTuples[i+1]])
    else:
        colorShifts.append([colorRGBTuples[i], colorRGBTuples[0]])


while True:
    for fromRGB, toRGB in colorShifts:
        #setting shifts for current color transition
        shiftLengthR =  (toRGB[0]-fromRGB[0]) if toRGB[0]-fromRGB[0] != 0 else 1
        shiftLengthG =  (toRGB[1]-fromRGB[1]) if toRGB[1]-fromRGB[1] != 0 else 1
        shiftLengthB =  (toRGB[2]-fromRGB[2]) if toRGB[2]-fromRGB[2] != 0 else 1
        for i in range(loopTime):
            # divide to get the ratio of loops to single bit color shift ratio,
            # then floor the current loop to find how many color bits should be shifted on this loop
            addValueR = i//(loopTime/shiftLengthR)
            addValueG = i//(loopTime/shiftLengthG)
            addValueB = i//(loopTime/shiftLengthB)
            #set new colors
            pixels[0:4] = [((fromRGB[0] + addValueR), (fromRGB[1] + addValueG),(fromRGB[2] + addValueB))]*4
        