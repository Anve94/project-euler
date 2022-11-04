"""
Problem 1: If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples
is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solution1(n: list) -> int:
    """Verbose solution by doing the checks directly."""
    total = 0
    for value in n:
        if value % 3 == 0:
            total += value
        elif value % 5 == 0:
            total += value
            
    return total

def solution2(n: list) -> int:
    """Same as first solution but with list comprehension"""
    return sum([i for i in n if i % 3 == 0 or i % 5 == 0])

def solution3() -> int:
    """Different solution by summing all values divisble by 3 and
    5 and substracting the shared 15
    """
    threes =  [i for i in range(3, 1000, 3)]
    fives = [i for i in range(5, 1000, 5)]
    fifteens = [i for i in range(15, 1000, 15)]
    
    return sum(threes) + sum(fives) - sum(fifteens)

if __name__ == '__main__':
    n = [i for i in range(1, 1000)]

    print(solution1(n))
    print(solution2(n))
    print(solution3())