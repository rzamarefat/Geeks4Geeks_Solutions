"""
Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
Note: You have to return 1 if it is possible to convert the given string into palindrome else return 0. 

Example 1:

Input:
S = "geeksogeeks"
Output: Yes
Explanation: The string can be converted
into a palindrome: geeksoskeeg

Example 2:

Input: 
S = "geeksforgeeks"
Output: No
Explanation: The given string can't be
converted into a palindrome.
"""


def is_possible(string):    
    is_possible_or_not = True
    if not(len(string) % 2 == 0):
        print(f"1The string {string} cannot be rearranged to be a palindrome.")
        exit()


    data = {}
    for s in string:
        counter = 0
        for s_ in string:
            if s_ == s:
                counter += 1
        data[s] = counter
    for value in data.values():
        if not(value % 2 == 0):
            is_possible_or_not = False

    
    if is_possible_or_not:
        print(f"3The string {string} can be rearranged to be a palindrome.")
    else:
        print(f"3The string {string} cannot be rearranged to be a palindrome.")
        
if __name__ == "__main__":
    string = "geeksgeeks"
    is_possible(string)