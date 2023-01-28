"""
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

If there are multiple solutions, find the lexicographically smallest one.

Example 1:

Input:
n = 5
arr[] = {1,2,3,4,5}
Output: 2 1 4 3 5
Explanation: Array elements after 
sorting it in wave form are 
2 1 4 3 5.
Example 2:

Input:
n = 6
arr[] = {2,4,7,8,9,10}
Output: 4 2 8 7 10 9
Explanation: Array elements after 
sorting it in wave form are 
4 2 8 7 10 9.
"""

def sort_wavy(array):
    wavy_sorted_array = []
    
    for i in range(len(array) // 2):
        if array[i * 2: (i + 1)*2][0] < array[i * 2: (i + 1)*2][1]:
            wavy_sorted_array.append(array[i * 2: (i + 1)*2][1])
            wavy_sorted_array.append(array[i * 2: (i + 1)*2][0])
        else:
            wavy_sorted_array.append(array[i * 2: (i + 1)*2][0])
            wavy_sorted_array.append(array[i * 2: (i + 1)*2][1])
    
    remaining_number = len(array) - len(wavy_sorted_array)
    print("remaining_number", remaining_number)
    for i in range(0, remaining_number):
        print(len(array) - remaining_number)
        print(array[-1* i])
        wavy_sorted_array.append(array[-1* i])
    

    print(wavy_sorted_array)
    # print(remaining)



    print(f"The wavy sorted array: {wavy_sorted_array}")
if __name__ == "__main__":
    array = [1,2,3,4,5]
    # array = [2,4,7,8,9,10]
    sort_wavy(array)