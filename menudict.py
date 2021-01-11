
def func_a():
    print("func a")


def func_b():
    print("func b")


def func_c():
    print("func c")


def func_d():
    print("func d")

def main():
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

if __name__ == "__main__":
    main()