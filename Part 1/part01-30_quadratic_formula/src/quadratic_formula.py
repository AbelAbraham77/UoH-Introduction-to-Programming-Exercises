from math import sqrt

a=int(input("Value of a: "))
b=int(input("Value of b: "))
c=int(input("Value of c: "))

x=(-b + (sqrt(b**2 - 4*a*c)))/(2*a)
y=(-b - (sqrt(b**2 - 4*a*c)))/(2*a)

print(f"The roots are {x} and {y}")