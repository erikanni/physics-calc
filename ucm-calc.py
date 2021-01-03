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
            return T, "N"
        elif v == "":
            W = float(m) * 9.8 
            m = float(m)
            r = float(r)
            T = float(T)
            v = math.sqrt(((T - W)*r)/m)
            return v, "m/s"
        elif r == "": 
            W = float(m) * 9.8 
            m = float(m)
            v = float(v)
            T = float(T)
            r = (m*v*v)/(T - W)
            return r, "m"
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
            return T, "N"
        elif v == "":
            W = float(m) * 9.8 
            m = float(m)
            r = float(r)
            T = float(T)
            v = math.sqrt(((T + W)*r)/m)
            return v, "m/s"
        elif r == "": 
            W = float(m) * 9.8 
            m = float(m)
            v = float(v)
            T = float(T)
            r = (m*v*v)/(T + W)
            return r, "m"

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
            return T, "N"
        elif r == "": 
            W = float(m) * 9.8 
            m = float(m)
            v = float(v)
            T = float(T)
            r = (m*v*v)/T
            return (r, "m")

        elif v == "":
            W = float(m) * 9.8 
            m = float(m)
            r = float(r)
            T = float(T)
            v = math.sqrt((T*r)/m)
            return (v, "m/s")
    else:
        print("that is an invalid input")
        return



result, units = solve()
print(f"the result is {result:.3f} {units}")
