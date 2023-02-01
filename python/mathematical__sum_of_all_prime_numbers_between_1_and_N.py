"""
Given a positive integer N, find the sum of all prime numbers between 1 and N(inclusive).

Example 1:

Input: N = 5
Output: 10
Explanation: 2, 3, and 5 are prime
numbers between 1 and 5(inclusive).
Example 2:

Input: N = 10
Output: 17
Explanation: 2, 3, 5 and 7 are prime
numbers between 1 and 10(inclusive).

"""

def find_if_is_prime(num):
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    
    return is_prime
    


def main(N):
    prime_nums = [N]
    for i in range(2, N+1):

        if i in prime_nums:
            continue
            
        if find_if_is_prime(i):
            prime_nums.append(i)

    print(f"The sum of all prime numbers from 1 to {N} is {sum(prime_nums)}")


if __name__ == "__main__":
    main(5) #1, 2, 3, 5, 7
