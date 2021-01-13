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
        result = str(float(mass * acceleration)) + "N"
        
    elif mass == "":
        force = float(force)
        acceleration = float(acceleration)
        result = str(float(force/acceleration)) + "kg"
        
    elif acceleration == "":
        mass = float(mass)
        force = float(force)
        result = str(float(force/mass)) + "m/s^2"
        
    else:
        print("incorrect usage")
        sys.exit(1)
        
    print(result)

def main():
    sp.call('clear',shell=True)
    solve()


def func_d():
    print("func d")

#def main():
    print('''
    function a
    function b
    function c
    function d
    ''')
    menu_dict = {"a": func_a, "b": func_b, "c": func_c, "d": func_d}
    answer = input("select function: ").lower()[0]
    if answer in menu_dict:
        menu_dict[answer]()
    else:
        print("No such function")

if __name__ == '__main__':
    main()

    
