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

def solve2():
    print("leave blank for item that is unknown")
    a = input("enter a: ")
    r = input("enter r: ")
    alpha = input("enter alpha: ")
    
    if a == "":
        alpha = float(alpha)
        r = float(r)
        result = str(float(alpha * r)) + "m/s^2"
        
    elif alpha == "":
        r = float(r)
        a = float(a)
        result = str(float(a/r)) + "rad/s^2"
        
    elif r == "":
        alpha = float(alpha)
        a = float(a)
        result = str(float(a/alpha)) + "m"
        
    else:
        print("incorrect usage")
        sys.exit(1)
        
    print(result)

def solve3():
    print("leave blank for item that is unknown")
    s = input("enter s: ")
    r = input("enter r: ")
    theta = input("enter theta: ")
    
    if s == "":
        theta = float(theta)
        r = float(r)
        result = str(float(theta * r)) + "m/s^2"
        
    elif theta == "":
        r = float(r)
        s = float(s)
        result = str(float(s/r)) + "rad/s^2"
        
    elif r == "":
        theta = float(theta)
        s = float(s)
        result = str(float(s/theta)) + "m"
        
    else:
        print("incorrect usage")
        sys.exit(1)
        
    print(result)
