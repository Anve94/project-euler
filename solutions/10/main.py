"""
Problem 10: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from math import sqrt

def sieve_of_eratosthenes(limit: int) -> list:
    """Use Sieve of Eratosthenes to more efficiently calculate prime"""
    primes = {k:True for k in range(2, limit)}
    end = sqrt(limit)
    for i in primes.keys():
        if i >= end:
            break
        
        if primes.get(i) == True:
            for j in range(pow(i, 2), limit, i):
                primes[j] = False
            
    return primes

def generate_primes(limit: int) -> list:
    """Generate primes up to a value of limit"""
    found = [2]
    
    # Range steps 2 since primes > 2 are never even
    for value in range(3, limit + 1, 2):
        # Since all non-primes can be factorized into a product
        # of primes, we only have to check previous primes, I think
        if all(value % i != 0 for i in found):
            found.append(value)
            
    return found
    
if __name__ == '__main__':
    # Brute force takes 10m34s :(
    # primes = generate_primes(1999999)
    # print(sum(primes))
    
    # Sieve takes 0.7s :D
    primes = sieve_of_eratosthenes(2000000)
    total = sum([key for key, is_prime in primes.items() if is_prime])
    print(total)