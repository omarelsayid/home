for i in range(41):
    for s in range(41 - i):
        print(" ", end="")
    for j in range(1, (i*2 - 8) + 1):
        print("*", end="")
    print()

for rows in range(10):
    for columns in range(10):
        print(" *", end="")
    print("                        \t \t ", end="")
    for columns in range(10):
        print(" *", end="")
    print()
