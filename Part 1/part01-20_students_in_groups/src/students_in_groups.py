students=int(input("How many students on the course? "))
gsize=int(input("Desired group size? "))

if students//gsize==students/gsize:
    print(f"Number of groups formed: {students//gsize}")
else:
    print(f"Number of groups formed: {(students//gsize)+1}")

