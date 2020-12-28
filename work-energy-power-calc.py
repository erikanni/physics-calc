import math

def solve(choice):
    if choice == 1:
        work = (input("enter work: "))
        force = (input("enter force: "))
        displacement = (input("enter displacement: "))
        if work == "":
            force = float(force)
            displacement = float(displacement)

            work = force * displacement
            return work
        if force == "":
            work = float(work)
            displacement = float(displacement)

            force = work/displacement
            return force
        if displacement == "":
            work = float(work)
            force = float(force)

            displacement = work/force
            return displacement
    if choice == 3:
        power = input("enter power: ")
        work = input("enter work: ")
        time = input("enter time: ")
        if power == "":
            work = float(work)
            time = float(time)

            power = work/time
            return power
        if work == "":
            power = float(power)
            time = float(time)

            work = power * time
            return work
        if time == "":
            power = float(power)
            work = float(work)

            time = power * work
            return time

choice = int(input("enter 1 for work, 2 for energy, and 3 for power: "))
print(solve(choice))

