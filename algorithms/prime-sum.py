# Given a number, find out if two prime numbers will add up to equal the
# target number.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_sum_to_target(target):
    for i in range(2, target // 2 + 1):
        if is_prime(i) and is_prime(target - i):
            return True
    return False

# Time: O(nsqrt(n))
# Space: O(1)
