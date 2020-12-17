import math

print ("what variables are known?")
print("1: mass and acceleration")
print("2: force and acceleration")
print("3: mass and force")
choice = int(input("enter your choice"))

def solve():
    if choice == 1:
        mass = int(input("enter the mass"))
        acceleration = int(input("enter the acceleration"))
        result = mass * acceleration
    elif choice == 2:
        force = int(input("enter the force"))
        acceleration = int(input("enter the acceleration"))
        result = force/acceleration
    elif choice == 3:
        mass = int(input("enter the mass"))
        force = int(input("enter the force"))
        result = force/mass
    else:
        print("you must enter 1, 2 or 3")
        return

    print("the result is: " + result)

solve()