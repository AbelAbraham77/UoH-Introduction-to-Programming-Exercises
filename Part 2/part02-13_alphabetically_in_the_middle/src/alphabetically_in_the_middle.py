x=input("1st letter: ")
y=input("2nd letter: ")
z=input("3rd letter: ")

if x>y and x>z:
    if y>z:
        print(f"The letter in the middle is {y}")
    elif z>y:
        print(f"The letter in the middle is {z}")

elif y>x and y>z:
    if x>z:
        print(f"The letter in the middle is {x}")
    elif z>x:
        print(f"The letter in the middle is {z}")

elif z>x and z>y:
    if x>y:
        print(f"The letter in the middle is {x}")
    elif y>x:
        print(f"The letter in the middle is {y}")