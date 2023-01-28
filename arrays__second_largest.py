"""
Given an array Arr of size N, print second largest distinct element from an array.

Example 1:

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.
"""


def find_second_largest(array):
    biggest = array[0]
    second_largest = array[0]
    for a in array:
        if a > biggest:
           biggest = a
    
    for a in array:
        if a == biggest:
            continue

        if a > second_largest:
           second_largest = a

    print(f"The largest: {biggest} and the 2nd largest {second_largest}")


if __name__ == "__main__":
    array = [12, 35, 1, 10, 34, 1]
    find_second_largest(array)
