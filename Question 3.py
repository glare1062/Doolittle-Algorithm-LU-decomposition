from builtins import print

import numpy as np


def coordsBefore(x, y, z):
    t=(x-1)/2
    array=[]
    for i in range(0, 10):
        x= 1+2*t
        y = 1+6*t
        z = 1+14*t
        if (y == x ** 2 and z == x ** 3):
            print("found intercetion point at :" + str(x) + "," + str(y) + "," + str(z) + ",")
        array.append([x, y, z])
        t-=1

    return array


def coordsAfter(x, y, z):
    t = (x - 1) / 2
    array = []
    for i in range(0, 10):
        x = 1 + 2 * t
        y = 1 + 6 * t
        z = 1 + 14 * t
        if(y==x**2 and z==x**3):
            print("found intercetion point at :"+str(x)+","+str(y)+","+str(z)+",")
        array.append([x, y, z])
        t += 0.5

    return array


if __name__ == '__main__':
    x=0
    y=0
    z=0
    print("running before")
    num = coordsBefore(x, y, z)
    print(num)
    print("running after")
    num = coordsAfter(x, y, z)
    print(num)
