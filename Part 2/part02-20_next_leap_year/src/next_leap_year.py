year=int(input("Year: "))

if year%100==0:
    print(f"The next leap year after {year} is {year+4}")
elif year%4==0:
    if (year+4)%100==0 and (year+4)%400!=0:
        print(f"The next leap year after {year} is {year+8}")
    else:
        print(f"The next leap year after {year} is {year+4}")
elif year%4==1:
    if (year+3)%100==0 and (year+3)%400!=0:
        print(f"The next leap year after {year} is {year+7}")
    else:
        print(f"The next leap year after {year} is {year+3}")
elif year%4==2:
    if (year+2)%100==0 and (year+2)%400!=0:
        print(f"The next leap year after {year} is {year+6}")
    else:
        print(f"The next leap year after {year} is {year+2}")
elif year%4==3:
    if (year+1)%100==0 and (year+1)%400!=0:
        print(f"The next leap year after {year} is {year+5}")
    else:
        print(f"The next leap year after {year} is {year+1}")