"""
Problem 4: A palindromic number reads the same both ways
The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 x 99. Find the largest palindrome
made from the product of two 3-digit numbers.
"""

def largest_palindrome() -> int:
    """Find the largest palindrome as a result
    of two 3-digit numbers.
    """
    x = [i for i in range(100, 1000)]
    found = []
    
    for i in x:
        for j in x:
            to_check = i * j
            if is_palindrome(to_check):
                found.append(to_check)
                
    return max(found)
                
            
    
def is_palindrome(n: int) -> bool:
    """Check whether the number is a palindrome by casting to string
    and comparing the string to itself when it's reversed.
    """
    return (str(n) == str(n)[::-1])

if __name__ == '__main__':
    """Complexity is O(n^2) but computers are very fast these days"""
    largest = largest_palindrome()
    print(largest)