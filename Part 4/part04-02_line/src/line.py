# Write your solution here
def line(num, str):
    if len(str)!=0:
        print(str[0]*num)
    else:
        print("*"*num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")