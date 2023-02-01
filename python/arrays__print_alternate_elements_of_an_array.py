"""
You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).

Example 1:

Input:
N = 4
A[] = {1, 2, 3, 4}
Output:
1 3
Example 2:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
1 3 5
"""


def print_alternate_elements(N):
    for i in range(N+1):
        if not(i % 2 == 0):
            print(i)
        


if __name__ == "__main__":
    N = 5
    print_alternate_elements(N)