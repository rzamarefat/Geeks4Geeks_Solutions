"""
Given two numbers A and B, find Kth digit from right of AB.
 

Example 1:

Input:
A = 3
B = 3
K = 1
Output:
7
Explanation:
33 = 27 and 1st
digit from right is 
7
Example 2:

Input:
A = 5
B = 2
K = 2
Output:
2
Explanation:
52 = 25 and second
digit from right is
2.

Your Task:
You don't need to read input or print anything. Your task is to complete the function kthDigit() which takes integers A, B, K as input parameters and returns Kth Digit of AB from right side.
"""


def find_kth_digit(base, power, k):

    required = str(base ** power)[-k]

    print(f"The {k} th digit of {base} to the power of {power} is {required}")

if __name__ == "__main__":
    find_kth_digit(3, 3, 1)
    find_kth_digit(5, 2, 2)