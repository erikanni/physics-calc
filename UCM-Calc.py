import math

def solve():
    choice = 0
    print("1: Highest Point")
    print("2: Lowest Point")
    print("3: Half Way")
    choice = int(input("enter your choice: "))

    if choice == 1:
        T = (input("enter tension: "))
        m = (input("enter mass: "))
        v = (input("enter velocity: "))
        r = (input("enter radius: "))

        if T == "":
            W = float(m) * 9.8
            m = float(m)
            v = float(v)
            r = float(r)
            T = (m*(v*v))/r+W
            result = str(T)
        elif v == "":
            W = float(m) * 9.8 
            m = float(m)
            r = float(r)
            T = float(T)
            v = math.sqrt((T/m*v)/r+W)
            result = str(v)
        elif r == "": #needs a lot of fixing
            W = float(m) * 9.8 
            m = float(m)
            v = float(v)
            T = float(T)
            r = (m*(v*v))/T - W
            result = str(r)
    elif choice == 2:
        T = (input("enter tension: "))
        m = (input("enter mass: "))
        v = (input("enter velocity: "))
        r = (input("enter radius: "))

        if T == "":
            W = float(m) * 9.8
            m = float(m)
            v = float(v)
            r = float(r)
            T = (m*(v*v))/r-W
            result = str(T)
        elif v == "":
            W = float(m) * 9.8 
            m = float(m)
            r = float(r)
            T = float(T)
            v = math.sqrt((T/m*v)/r-W)
            result = str(v)
        elif r == "": #needs a lot of fixing
            W = float(m) * 9.8 
            m = float(m)
            v = float(v)
            T = float(T)
            r = (m*(v*v))/T + W
            result = str(r)

    elif choice == 3:
        T = (input("enter tension: "))
        m = (input("enter mass: "))
        v = (input("enter velocity: "))
        r = (input("enter radius: "))
        if T == "":
            W = float(m) * 9.8
            m = float(m)
            v = float(v)
            r = float(r)
            T = (m*(v*v))/r
            result = str(T)
        elif r == "": ## needs a lot of fixing
            W = float(m) * 9.8 
            m = float(m)
            v = float(v)
            T = float(T)
            r = (m*(v*v))/T
            result = str(r)

        elif v == "":
            W = float(m) * 9.8 
            m = float(m)
            r = float(r)
            T = float(T)
            v = math.sqrt(T/m*v)/r 
            result = str(v)
    else:
        print("that is an invalid input")
        return

    print("the unknown variable is " + result)
solve()