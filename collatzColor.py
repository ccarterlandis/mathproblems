import random

import matplotlib.pyplot as plt

inumfor = []
inumflip = []
ivalfor = []
ivalback = []
iforflipped = []
ibackflipped = []


def Collatz(query):
    i = query
    inumfor.append(i)
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            inumfor.append(i)
        else:
            i = 3 * i + 1
            inumfor.append(i)


def Collatzflipped(query):
    i = query
    inumflip.append(160 - i)
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            inumflip.append(160 - i)
        else:
            i = 3 * i + 1
            inumflip.append(160 - i)


for i in range(1, 20, 1):
    inumfor = []
    inumflip = []
    Collatz(i)
    Collatzflipped(i)
    ivalfor.append(inumfor)
    ivalback.append(inumfor[::-1])
    iforflipped.append(inumflip)
    ibackflipped.append(inumflip[::-1])

plt.subplot(111, facecolor='black')

width = 3
color1 = (random.random())
color2 = (random.random())
color3 = (random.random())

for item in ivalback:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

for item in ivalfor:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

for item in iforflipped:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

for item in ibackflipped:
    plt.plot(item, color=(color1, color2, color3), linewidth=width)
    color1 = (random.random())
    color2 = (random.random())
    color3 = (random.random())

plt.show()
