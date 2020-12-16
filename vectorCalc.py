import math


def addVectors(vector1mag, vector1deg, vector2mag, vector2deg):
    xcomp1 = (math.cos(math.radians(vector1deg))) * vector1mag
    ycomp1 = (math.sin(math.radians(vector1deg))) * vector1mag

    xcomp2 = (math.cos(math.radians(vector2deg))) * vector2mag
    ycomp2 = (math.sin(math.radians(vector2deg))) * vector2mag


    xMagTotal = xcomp1 + xcomp2
    yMagTotal = ycomp1 + ycomp2

    hyp = math.sqrt(math.pow(xMagTotal, 2) + math.pow(yMagTotal, 2))
    deg = math.degrees(math.atan2(yMagTotal, xMagTotal))

    return (hyp, deg)

def subtractVectors(vector1mag, vector1deg, vector2mag, vector2deg):
    xcomp1 = (math.cos(math.radians(vector1deg))) * vector1mag
    ycomp1 = (math.sin(math.radians(vector1deg))) * vector1mag

    xcomp2 = (math.cos(math.radians(vector2deg))) * vector2mag
    ycomp2 = (math.sin(math.radians(vector2deg))) * vector2mag


    xMagTotal = xcomp1 - xcomp2
    yMagTotal = ycomp1 - ycomp2

    hyp = math.sqrt(math.pow(xMagTotal, 2) + math.pow(yMagTotal, 2))
    deg = math.degrees(math.atan2(yMagTotal, xMagTotal))

    return (hyp, deg)


v1mag = int(input("Vector 1 Magnitude: "))
v1deg = int(input("Vector 1 degree: "))

v2mag = int(input("Vector 2 Magnitude: "))
v2deg = int(input("Vector 2 degree: "))

(vsummag, vsumdeg) = addVectors(v1mag, v1deg, v2mag, v2deg)
print(vsummag + "  " + vsumdeg)