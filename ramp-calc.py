import math

G_CONSTANT = 9.81

def solve(choice):
    if choice == 1:
        mass = float(input("mass: "))
        uk = float(input("friction coefficient: "))
        theta = float(input("angle (degrees): "))
        normal = (math.cos(theta)* mass * G_CONSTANT)
        Ff = normal * uk
        return Ff
    if choice == 2:
        mass = float(input("mass: "))
        theta = float(input("angle (degrees): "))
        Fa = (math.sin(math.radians(theta)) * mass * G_CONSTANT)
        return Fa
    if choice == 3:
        mass = float(input("mass: "))
        uk = float(input("friction coefficient: "))
        theta = float(input("angle (degrees): "))
        normal = (math.cos(math.radians(theta))* mass * G_CONSTANT)
        Ff = normal * uk
        Fa = (math.sin(math.radians(theta)) * mass * G_CONSTANT)
        net = Fa - Ff
        return net


print("1: calculate force of friction")
print("2: calculate paralell force")
print("3: calculate net force")
choice = int(input("enter your choice: "))
print(f"{solve(choice):.3f}")

