import math

def solve():
    choice = int(input("enter 1 for rev, 2 for deg, or 3 for rad"))
    if choice == 1:
        rev = float(input("enter rev"))
        deg = rev * 360
        rad = deg * math.pi/180
        print("deg: " + str(deg))
        print("rad: " + str(rad))

    if choice == 2:
        deg = float(input("enter degrees"))
        rev = deg/360
        rad = deg*math.pi/180
        print("rev: " + str(rev))
        print("rad: " + str(rad))#TODO

    if choice == 3:
        rad = float((input("enter rad")))
        deg = rad*180/math.pi
        rev = deg/360 
        print("deg: " + str(deg))
        print("rev: " + str(rev))
        
   
def kinematics():
    #TODO 
    #make kinematics
    a = float(input("a: "))
    vi = float(input("vi: "))
    X = float(input("X: "))
    t = float(input("t: "))
    vf = float(input("vf: "))

    



solve()
