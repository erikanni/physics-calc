import math
import sys
import subprocess as sp


def solve():
    print("leave blank for item that is unknown")
    force = input("enter force: ")
    mass = input("enter mass: ")
    acceleration = input("enter acceleration: ")
    
    if force == "":
        mass = float(mass)
        acceleration = float(acceleration)
        result = str(float(mass * acceleration)) + " N"
        
    elif mass == "":
        force = float(force)
        acceleration = float(acceleration)
        result = str(float(force/acceleration)) + " kg"
        
    elif acceleration == "":
        mass = float(mass)
        force = float(force)
        result = str(float(force/mass)) + " m/s^2"
        
    else:
        print("incorrect usage")
        sys.exit(1)
        
    print(result)

def main():
    sp.call('clear',shell=True)
    solve()


if __name__ == '__main__':
    main()

    
