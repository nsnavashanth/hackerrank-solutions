# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/mathematical-algorithms-prime-security-checkpoints/problem?isFullScreen=true
# Problem     Mathematical Algorithms - Prime Security Checkpoints
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 09:25 a.m.
# Technique   trial-division-primality-test
# Time        O((end-start) * sqrt(end))
# Space       O(end-start)
# Insight     The algorithm iterates through the inclusive range and validates each integer using trial division up to its square root, skipping multiples of two and three to optimize the check.
# Interview   Before: "I would iterate through the range and check each number for primality." After: "I implemented a trial division approach with O((end-start) * sqrt(end)) time complexity, ensuring that numbers less than two are correctly excluded as per the problem constraints."
# Pitfalls    (1) Failing to handle the inclusive range correctly by using range(start, end) instead of range(start, end + 1).  (2) Incorrectly identifying 1 as a prime number, which violates the mathematical definition of primality.  (3) Neglecting to handle the case where no primes exist in the range, which requires printing nothing.
# ──────────────────────────────────────────────────

import sys

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start = int(input_data[0])
    end = int(input_data[1])
    
    primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
    
    if primes:
        print(" ".join(primes))

if __name__ == "__main__":
    main()
