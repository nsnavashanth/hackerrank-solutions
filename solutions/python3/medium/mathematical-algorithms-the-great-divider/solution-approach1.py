# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/mathematical-algorithms-the-great-divider/problem?isFullScreen=true
# Problem     Mathematical Algorithms - The Great Divider
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-04, 09:01 a.m.
# ──────────────────────────────────────────────────

import math
import sys


def solve_vault_lock():
    # Fast I/O for large inputs (n up to 10^5)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    guardian_numbers = [int(x) for x in input_data[1 : n + 1]]

    # Initialize GCD with the first guardian number
    current_gcd = guardian_numbers[0]

    # Iteratively compute the GCD across all guardian numbers
    for num in guardian_numbers[1:]:
        current_gcd = math.gcd(current_gcd, num)
        # Early exit optimization: GCD cannot go below 1
        if current_gcd == 1:
            break

    print(current_gcd)


if __name__ == "__main__":
    solve_vault_lock()
