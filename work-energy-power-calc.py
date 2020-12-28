import math

def solve(choice):
    if choice == 1:
        work = (input("enter work: "))
        force = (input("enter force: "))
        displacement = (input("enter displacement: "))
        if work == "":
            force = float(force)
            displacement = float(displacement)

            work = str(force * displacement) + " J"
            return work
        if force == "":
            work = float(work)
            displacement = float(displacement)

            force = str(work/displacement) + " N"
            return force
        if displacement == "":
            work = float(work)
            force = float(force)

            displacement = str(work/force) + " m"
            return displacement

    if choice == 2:
        print("this section is not currently finished")
        #work in progress

    if choice == 3:
        power = input("enter power: ")
        work = input("enter work: ")
        time = input("enter time: ")
        if power == "":
            work = float(work)
            time = float(time)

            power = str(work/time) + " Watts"
            return power
        if work == "":
            power = float(power)
            time = float(time)

            work = str(power * time) + " J"
            return work
        if time == "":
            power = float(power)
            work = float(work)

            time = str(power * work) + " s"
            return time

print("leave blank for the value you want to calculate")
choice = int(input("enter 1 for work, 2 for energy, and 3 for power: "))
print(solve(choice))

