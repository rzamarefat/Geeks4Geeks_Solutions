"""
Given a string S, check if it is palindrome or not.

Example 1:

Input: S = "abba"
Output: 1
Explanation: S is a palindrome
Example 2:

Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome
"""


def is_palindrome(string):
    is_palindrome_or_not = True
    for index, s in enumerate(string):
        if not(s == string[len(string) - index - 1]): 
            is_palindrome_or_not = False
            break

    if is_palindrome_or_not: print(f"String '{string}' is palindrome.")
    else: print(f"String '{string}' is not palindrome.")

        
if __name__ == "__main__":
    string = "ABBA"
    #string = "ASA"
    #string = "sunday"
    is_palindrome(string)