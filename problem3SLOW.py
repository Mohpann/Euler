# Connor Hunter
# November 8th 2022

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def getFactors(num):
    factors = []
    for potentialFactor in range(1, num+1): # really slow
        if num % potentialFactor == 0:
            factors.append(potentialFactor) # is factors of num
    return factors

def isPrime(num):
    return len(getFactors(num)) == 2

factors = getFactors(600851475143)
largestPrimeFactor = 0

for factor in factors:
    if isPrime(factor) and factor > largestPrimeFactor: # if factor is prime AND larger than curr largestPrimeFactor
        largestPrimeFactor = factor

print(largestPrimeFactor)
