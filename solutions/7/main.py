"""
Problem 7: By listing the first six prime numbers: 2, 3, 5,
7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def get_nth_prime(n: int) -> int:
    counter = 2
    last = 3 # Start on first odd prime so we can incr. by 2 later
    while counter < n:
        prime = next_prime(last)
        last = prime
        counter += 1
            
    return prime

def next_prime(last: int) -> int:
    """Woo! Recursion"""
    check = last + 2 # Increase by 2 since primes > 2 are never even!
    if is_prime(check):
        return check
    
    return next_prime(check)

def is_prime(n: int) -> bool:
    return all(n % i != 0 for i in range(2, n))

if __name__ == '__main__':
    """Brute-force (30s runtime...) solution to get nth prime when only generating primes"""
    print(get_nth_prime(10001))