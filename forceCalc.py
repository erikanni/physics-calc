import math
import sys
import subprocess as sp


def solveImproved():
    print("leave blank for item that is unknown")
    force = input("enter force: ")
    mass = input("enter mass: ")
    acceleration = input("enter acceleration: ")
    if force == "":
        mass = float(mass)
        acceleration = float(acceleration)
        result = float(mass * acceleration)
    elif mass == "":
        force = float(force)
        acceleration = float(acceleration)
        result = float(force/acceleration)
    elif acceleration == "":
        mass = float(mass)
        force = float(force)
        result = float(force/mass)
    else:
        print("incorrect usage")
        sys.exit(1)
    print(result)

def main():
    sp.call('clear',shell=True)
    solveImproved()


if __name__ == '__main__':
    main()