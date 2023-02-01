"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other.

Example 1:

Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with
        same frequency. So, both are anagrams.
Example 2:

Input:a = allergy, b = allergic
Output: NO
Explanation: Characters in both the strings are 
        not same, so they are not anagrams.
"""


def is_anagram(string_one, string_two):
    is_anagram_or_not = True

    if not(len(string_one) == len(string_two)):
        is_anagram_or_not = False
        print(f"1string one: {string_one} string_two: {string_two} -> they are not anagram.")
        exit()

    for c in string_one:
        if not(c in string_two):
            print(f"2string one: {string_one} string_two: {string_two} -> they are not anagram.")
            exit()
        else:
            string_one = string_one.replace(c, "")

    print(f"3string one: {string_one} string_two: {string_two} -> they are anagram.")



if __name__ == "__main__":
    string_1 = "geeksforgeeks"
    string_2 = "forgeeksgeeks"
    is_anagram(string_1, string_2)


