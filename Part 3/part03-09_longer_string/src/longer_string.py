str1=input("Please type in string 1: ")
str2=input("Please type in string 2: ")
n1, n2=len(str1), len(str2)

if n1>n2:
    print(f"{str1} is longer")
elif n2>n1:
    print(f"{str2} is longer")
else:
    print("The strings are equally long")