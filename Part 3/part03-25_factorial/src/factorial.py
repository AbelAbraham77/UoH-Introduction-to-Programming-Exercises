while True:
    num=int(input("Please type in a number: "))
    if num<=0:
        print("Thanks and bye!")
        break

    else:
        fact=1
        for i in range(1,num+1):
            fact*=i
        print(f"The factorial of the number {num} is {fact}")
        