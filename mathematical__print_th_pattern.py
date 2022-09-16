
# You a given a number N. You need to print the pattern for the given value of N.

# For N = 2 the pattern will be 
# 2 2 1 1
# 2 1

# For N = 3 the pattern will be 
# 3 3 3 2 2 2 1 1 1
# 3 3 2 2 1 1
# 3 2 1

# ==========================

N = int(input("Give N (and iteger number)"))

print("The required: ")
for i in range(N):
    for j in range(N):
        for x in range(N - i):
            print(N - j, end=" ")
    print(" ")