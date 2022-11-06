"""
Problem 9: A Pythagorean triplet is a set of three natural
numbers, a < b < c, for which,

        a^2 + b^2 = c^2
    
For example,

        3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

def find_triplet(n: int) -> tuple:
    for b in range(1, n + 1):
        for a in range(1, n + 1):
            temp = a**2 + b**2
            c = sqrt(temp)
            
            if not c.is_integer():
                continue
            
            if not a < b < c:
                continue
            
            if a + b + c == n:
                return (a, b, c)
    
    raise ValueError('Woopsie')
    
if __name__ == '__main__':
    a, b, c = find_triplet(1000)
    print(int(a * b * c))
