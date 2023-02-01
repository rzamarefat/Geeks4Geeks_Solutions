"""
https://practice.geeksforgeeks.org/problems/pair-cube-count4132/1

Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = N.

 
Example 1:

Input:
N = 9 
Output:
2
Explanation:
There are two solutions: (a=1, b=2)
and (a=2, b=1).

Example 2:

Input:
N = 27
Output:
1
Explanation:
Thereis only one solution: (a=3, b=0)

"""

def find_pair_cube(N):
    solutions = []


    for b in range(0, N):
        a = (N - b ** 3) ** (1. / 3)

        try:
            if a - int(a) == 0:
                if not(int(a) == 0):
                    solutions.append((int(a), b))
        except:
            continue
    

    print(f"There are {len(solutions)} solutions and they are {solutions}")

if __name__ == "__main__":
    # find_pair_cube(9)
    find_pair_cube(27)
