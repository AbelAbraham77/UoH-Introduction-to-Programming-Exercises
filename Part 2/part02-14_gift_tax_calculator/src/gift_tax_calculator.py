val=int(input("Value of gift: "))

if val<5000:
    print("No tax!")
elif 5000<=val<25000:
    print(f"Amount of tax: {100 + ((val-5000)*0.08)}")
elif 25000<=val<55000:
    print(f"Amount of tax: {1700 + ((val-25000)*0.1)}")
elif 55000<=val<200000:
    print(f"Amount of tax: {4700 + ((val-55000)*0.12)}")
elif 200000<=val<1000000:
    print(f"Amount of tax: {22100 + ((val-200000)*0.15)}")
elif val>=1000000:
    print(f"Amount of tax: {142100 + ((val-1000000)*0.17)}")