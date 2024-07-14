#Connor Hunter

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(num):
    string_num = str(num)
    return string_num == string_num[::-1] # is the number reversed the same as the original number? 

def find_largest_palindrome():
    curr_largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if i*j > curr_largest_palindrome:
                if (isPalindrome(i*j)):
                    curr_largest_palindrome = i*j
    return curr_largest_palindrome

print(find_largest_palindrome())