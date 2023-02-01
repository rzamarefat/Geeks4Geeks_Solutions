"""
Given two positive numbers X and Y, check if Y is a power of X or not.

Example 1:

Input:
X = 2, Y = 8
Output:
1
Explanation:
2^3 is equal to 8.
 

Example 2:

Input:
X = 1, Y = 3
Output:
0
Explanation:
Any power of 1 is not 
equal to 8.
"""

def main(x, y):
    original_x = x
    is_its_power = True
    while True:
        if x < y:
            break

        if x % y == 0:
            x /= y
        else:
            is_its_power = False
            break
    
    if is_its_power:
        print(f"Number {original_x} is a power of {y}")
    else:
        print(f"Number {original_x} is not a power of {y}")

    

if __name__ == "__main__":
    x = 81
    y = 3 
    main(x, y)