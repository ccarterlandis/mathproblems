import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import cm


sequence = [1]

n = 0

while n < 20:
    sequence.append(sequence[n] + sequence[n-1])
    n += 1

psequence = []
pseqflip = []
pisano = 1
plist = []
plistback = []
plistflip = []
pflipback = []

for y in range(10):
    for item in sequence:
        if item % pisano != 0:
            psequence.append(item % pisano)
            pseqflip.append(item % pisano)

    pisano += 1
    plist.append(psequence)
    plistback.append(psequence[::-1])
    for item in psequence:
        plistflip.append(9-item)
    for item in psequence[::-1]:
        pflipback.append(9-item)
    psequence = []

plt.subplot(111, axisbg='black')

width = 2
color1 = (random.random())
color2 = (random.random())
color3 = (random.random())

for item in plist:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

for item in plistback:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

for item in plistflip:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

for item in pflipback:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())


plt.show()




