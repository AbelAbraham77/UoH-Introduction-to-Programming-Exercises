# Copy here code of line function from previous exercise
def line(num, str):
    if len(str)!=0:
        print(str[0]*num)
    else:
        print("*"*num)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    for i in range (0, size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
