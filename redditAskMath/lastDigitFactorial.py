'''
Connor Hunter
7/17/24
Response to a question on reddit.com/r/askmath

The value of 30! is computed and all the ending digits "0" are removed from the result. What is the last digit of the remaining value?
'''
import math

# NOT USING -> Built in factorial method is faster
# def calculate_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return (n * calculate_factorial(n-1))

def get_last_nonzero_digit(f):
    # Loop backwards through stringified factorial
    for i in range(len(f) - 1, -1, -1):
        # Once we find a non-zero digit return the digit
        if not(f[i] == '0'):
            return f[i]

if __name__ == "__main__":
    # Type cast factorial of 30 to string so we can loop through it
    print(get_last_nonzero_digit(str(math.factorial(30))))