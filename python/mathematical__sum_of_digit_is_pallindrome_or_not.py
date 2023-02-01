"""
Sum of Digit is Pallindrome or not

Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.
Note:A Palindrome number is a number which stays the same when reversed.Example- 121,131,7 etc.

Example 1:

Input:
N=56
Output:
1
Explanation:
The digit sum of 56 is 5+6=11.
Since, 11 is a palindrome number.Thus,
answer is 1.
Example 2:

Input:
N=98
Output:
0
Explanation:
The digit sum of 98 is 9+8=17.
Since 17 is not a palindrome,thus, answer
is 0.   
"""

def find_if_palindrome(N):
    sum_of_digits = sum([int(digit) for digit in str(N)])
    
    target_number = [digit for digit in str(sum_of_digits)]
    

    is_palindrome = True
    for index, d in enumerate(target_number):
        if not(d == target_number[len(target_number) - index -1]):
            is_palindrome = False
    
    if is_palindrome:
        print(f"Number {N} is palindrome.")
    else:
        print(f"Number {N} is not palindrome.")

if __name__ == "__main__":
    find_if_palindrome(98)




