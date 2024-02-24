"""
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""


def find_largest_continuous_sum(arr):
    max_so_far = float("-inf")
    max_ending_here = 0

    for num in arr:
        
        max_ending_here += num

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    
    res = find_largest_continuous_sum(arr)

    print(res)