"""
Jumping Numbers

Given a positive number X. Find the largest Jumping Number smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

 

Example 1:

Input:
X = 10
Output:
10
Explanation:
10 is the largest Jumping Number
possible for X = 10.
Example 2:

Input:
X = 50
Output:
45
Explanation:
45 is the largest Jumping Number
possible for X = 50.
"""

def find_is_jumping_num(N):
    is_jumping_num = True
    for index, d in enumerate(str(N)):
        try:
            if not((int(d) - int(str(N)[index + 1]) == -1) or (int(d) - int(str(N)[index + 1]) == 1)):
                is_jumping_num = False
        except:
            continue

    return is_jumping_num

def find_largest_jumping_num(N):
    max_jumping_num = 0

    for n in range(1, N+1):
        
        if find_is_jumping_num(n) and max_jumping_num < n:
            max_jumping_num = n

    print(max_jumping_num)

if __name__ == "__main__":
    find_largest_jumping_num(14)