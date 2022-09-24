"""
You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow . Each test case contains four integers num1, den1, num2, den2 respectively .

Output Format:
For each test case, in a new line,  output will be the fraction in the form a/b where the fraction denotes the sum of the two given fractions in reduced form.

Constraints:
1 <= T <= 100
1 <= den1,den2,num1,num2 <= 1000

Example:
Input
1
1 500 2 500
Output
3/500

Explanation:
In above test case 1/500+2/500=3/500
"""


def add_two_fractions(num1, den1, num2, den2):
    if den1 == den2:
        nominator  = num1 + num2
        denominator = den1 
    else:
        nominator  = num1 * den2 + num2 * den1
        denominator = den1 * den2

    count = 2
    for i in range(2, min(nominator, denominator) // 2):
        if nominator % count == 0 and denominator % count == 0:
            nominator /= count
            denominator /= count

        count += 1 

    print(f"{int(nominator)}/{int(denominator)}")

if __name__ == "__main__":
    add_two_fractions(15, 35, 2, 3)

