# Determine if a number is a prime number

from math import sqrt


def is_prime(n):
    prime = 0
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime = 1
                break
        if not prime:
            return True
    return False

# Time: O(sqrt(n))
# Space: O(1)
