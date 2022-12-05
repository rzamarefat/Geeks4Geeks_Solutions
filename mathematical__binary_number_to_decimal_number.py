"""
Given a Binary Number B, find its decimal equivalent.
 

Example 1:

Input: B = 10001000
Output: 136
Example 2:

Input: B = 101100
Output: 44
"""

def convert_binary_to_decimal(binary_num):
    sum_ = 0
    for index, char in enumerate(str(binary_num)):
        if char == "1":
            sum_ += 2 ** (len(str(binary_num)) - index - 1)
    
    print(f"Binary Num: {binary_num} -> Decimal format: {sum_}")  

if __name__ == "__main__":
    convert_binary_to_decimal(10001000)