"""
Given N,  reverse the digits of N.
 

Example 1:

Input: 200
Output: 2
Explanation: By reversing the digts of 
number, number will change into 2.
Example 2:

Input : 122
Output: 221
Explanation: By reversing the digits of 
number, number will change into 221.
"""

def reverse_digits(num):
    inversed = []
    for index in range(len(str(num))-1, -1, -1):
        inversed.append(str(num)[index])

    print(f"The inversed number is: {int(''.join(inversed))}")
        

if __name__ == "__main__":
    reverse_digits(200)