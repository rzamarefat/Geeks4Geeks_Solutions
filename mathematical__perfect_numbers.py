"""
Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

 

Example 1:

Input:
N = 6
Output:
1 
Explanation:
Factors of 6 are 1, 2, 3 and 6.
Excluding 6 their sum is 6 which
is equal to N itself. So, it's a
Perfect Number.
Example 2:

Input:
N = 10
Output:
0
Explanation:
Factors of 10 are 1, 2, 5 and 10.
Excluding 10 their sum is 8 which
is not equal to N itself. So, it's
not a Perfect Number.
"""


def find_factors(num):
    i = 2
    factors = []
    while i ** 2 <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)

    return factors

def is_perfect_num(num):
    factors = set(find_factors(num))

    if sum(factors) + 1 == num:
        print(f"Number {num} is perfect.")
    else:
        print(f"Number {num} is not perfect.")

    

if __name__ == "__main__":
    is_perfect_num(6)
