"""
Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def factorize_prime(target: int) -> list:
    """Keep dividing the target with primes until the quotient is 1."""
    primes = generate_primes(10000)
    found = []
    for prime in primes:        
        if target % prime == 0:
            found.append(prime)
            target //= prime
            
        # Stop loop if quotient is 1
        if target == 1:
            break
        
    return found

def generate_primes(upper_limit: int) -> list:
    """Generate a bunch of primes since we need them for the factorization process"""
    found = []
    for value in range(2, upper_limit + 1):
        if all(value % i != 0 for i in range(2, value)):
            found.append(value)
            
    return found
        
    
if __name__ == '__main__':
    factored_primes = factorize_prime(600851475143)
    print(max(factored_primes))