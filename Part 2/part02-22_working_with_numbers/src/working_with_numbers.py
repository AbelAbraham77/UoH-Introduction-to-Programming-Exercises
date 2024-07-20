print("Please type in integer numbers. Type in 0 to finish.")
count=0 
sumnum=0 
pnum=0
nnum=0

while True:
    num=int(input("Number: "))
    if num==0:
        break
    count+=1
    sumnum+=num
    if num>0:
        pnum+=1
    elif num<0:
        nnum+=1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sumnum}")
print(f"The mean of the numbers is {sumnum/count}")
print(f"Positive numbers {pnum}")
print(f"Negative numbers {nnum}")