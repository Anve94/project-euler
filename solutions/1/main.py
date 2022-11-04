"""
Problem: If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples
is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_multiples(n: list) -> list:
    multiples = []
    for value in n:
        if value % 3 == 0:
            multiples.append(value)
        elif value % 5 == 0:
            multiples.append(value)
            
    return multiples
    
if __name__ == '__main__':
    n = [i for i in range(1, 1000)]
    print(sum(find_multiples(n)))