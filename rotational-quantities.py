import math

import sys
import subprocess as sp


def solve():
    print("leave blank for item that is unknown")
    w = input("enter w: ")
    r = input("enter r: ")
    v = input("enter v: ")
    
    if v == "":
        w = float(w)
        r = float(r)
        result = str(float(w * r)) + "m/s"
        
    elif w == "":
        r = float(r)
        v = float(v)
        result = str(float(v/r)) + "kg"
        
    elif r == "":
        w = float(w)
        v = float(v)
        result = str(float(v/w)) + "m"
        
    else:
        print("incorrect usage")
        sys.exit(1)
        
    print(result)
