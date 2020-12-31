import math
import sys
import subprocess as sp

def solve():
    print("Second object should be the one for which direction and velocity is known post collision")

    angle1 = float(input("enter the first angle"))
    angle2 = float(input("enter the second angle"))

    mass1 = float(input("enter the first mass"))
    velocity1 = float(input("enter the first velocity"))

    mass2 = float(input("enter the second mass"))
    velocity2 = float(input("enter the second velocity"))

    magResult1 = float(input("enter the result magnitude of one of the objects: "))
    degResult1 = float(input("enter the result degree of one of the objects: "))


    momentum1 = mass1 * velocity1
    momentum2 = mass2 * velocity2

    xcomp1 = (math.cos(math.radians(angle1))) * momentum1
    ycomp1 = (math.sin(math.radians(angle1))) * momentum1

    xcomp2 = (math.cos(math.radians(angle2))) * momentum2
    ycomp2 = (math.sin(math.radians(angle2))) * momentum2

    xMagTotal = xcomp1 + xcomp2
    yMagTotal = ycomp1 + ycomp2

    hyp = math.sqrt(math.pow(xMagTotal, 2) + math.pow(yMagTotal, 2))
    deg = math.degrees(math.atan2(yMagTotal, xMagTotal))

    resultxcomp1 = (math.cos(math.radians(deg))) * hyp
    resultycomp1 = (math.sin(math.radians(deg))) * hyp

    resultxcomp2 = (math.cos(math.radians(degResult1))) * magResult1
    resultycomp2 = (math.sin(math.radians(degResult1))) * magResult1

    resultxMagTotal = resultxcomp1 - resultxcomp2
    resultyMagTotal = resultycomp1 - resultycomp2

    Finalhyp = math.sqrt(math.pow(resultxMagTotal, 2) + math.pow(resultyMagTotal, 2))
    Finaldeg = math.degrees(math.atan2(resultyMagTotal, resultxMagTotal))

    velocityPostCollision = Finalhyp/mass2

    print("the magnitude of the other object's momentum is: " + str(Finalhyp) + "and the angle is: " + str(Finaldeg))
    print("the magnitude of the velocity of the object is: " + str(velocityPostCollision))

solve()













