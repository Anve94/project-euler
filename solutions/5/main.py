"""
Problem 5: 2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder. What is
the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""

def find_smallest():
    x = 20 # No need to start below 20 anyway
    while True:
        if is_divisible(x):
            return x
        x += 1
                
def is_divisible(n: int) -> bool:
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True
    

if __name__ == '__main__':
    """Takes over a minute :("""
    print(find_smallest())