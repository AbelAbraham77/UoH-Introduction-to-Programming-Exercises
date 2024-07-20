tempf=int(input("Please type in a temperature (F): "))
if tempf>=32:
    print(f"{tempf} degrees Fahrenheit equals {((tempf-32)*5)/9} degrees Celsius")
else:
    print(f"{tempf} degrees Fahrenheit equals {((tempf-32)*5)/9} degrees Celsius")
    print("Brr! It's cold in here!")
