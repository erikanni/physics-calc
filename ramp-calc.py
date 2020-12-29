import math

G_CONSTANT = 9.81

def solve(choice):
    if choice == 1:
        mass = float(input("mass: "))
        uk = float(input("friction coefficient: "))
        theta = float(input("angle (degrees): "))
        normal = (math.cos(theta)* mass * G_CONSTANT)
        Ff = str(normal * uk) + " N"
        return Ff
    if choice == 2:
        mass = float(input("mass: "))
        theta = float(input("angle (degrees): "))
        Fa = str((math.sin(math.radians(theta)) * mass * G_CONSTANT)) + " N"
        return Fa
    if choice == 3:
        mass = float(input("mass: "))
        uk = float(input("friction coefficient: "))
        theta = float(input("angle (degrees): "))
        normal = (math.cos(math.radians(theta))* mass * G_CONSTANT)
        Ff = normal * uk
        Fa = str((math.sin(math.radians(theta)) * mass * G_CONSTANT)) + " N"
        net = str(Fa - Ff) + " N"
        return net


print("1: calculate force of friction")
print("2: calculate paralell force")
print("3: calculate net force")
choice = int(input("enter your choice: "))
print(f"{solve(choice):.3f}")

