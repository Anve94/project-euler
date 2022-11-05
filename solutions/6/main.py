"""
Problem 6:
The sum of the squares of the first ten natural numbers is

        1^2 + 2^2 + 3^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

        (1 + 2 + 3 + ... 10)^2 = 55^ = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

        3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""  

if __name__ == '__main__':
    solution = pow(sum([i for i in range(1, 101)]), 2) - sum([pow(i, 2) for i in range(1, 101)])
    print(solution)