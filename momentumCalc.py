import math
import sys
import subprocess as sp

#same logic as forceCalc
def solve():
    print("leave blank for item that is unknown")
    momentum = input("enter momentum: ")
    mass = input("enter mass: ")
    velocity = input("enter velocity: ")
    if momentum == "":
        mass = float(mass)
        velocity = float(velocity)
        result = float(mass * velocity)
    elif mass == "":
        momentum = float(momentum)
        velocity = float(velocity)
        result = float(momentum/velocity)
    elif velocity == "":
        mass = float(mass)
        momentum = float(momentum)
        result = float(momentum/mass)
    else:
        print("incorrect usage")
        sys.exit(1)
    print(result)

def main():
    sp.call('clear',shell=True)
    solve()



if __name__ == '__main__':
    main()