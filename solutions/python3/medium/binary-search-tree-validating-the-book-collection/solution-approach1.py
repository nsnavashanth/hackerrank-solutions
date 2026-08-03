# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-search-tree-validating-the-book-collection/problem?isFullScreen=true
# Problem     Binary Search Tree - Validating the Book Collection
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:36 p.m.
# ──────────────────────────────────────────────────

from collections import deque
import sys


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        curr = queue.popleft()

        if i < len(values):
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
            i += 1

        if i < len(values):
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
            i += 1

    return root


def is_valid_bst(root, min_val=float("-inf"), max_val=float("inf")):
    if not root:
        return True

    if not (min_val < root.val < max_val):
        return False

    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(
        root.right, root.val, max_val
    )


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    values = [int(x) for x in input_data[1 : n + 1]]

    root = build_binary_tree(values)

    if is_valid_bst(root):
        print("The book collection is a valid binary search tree.")
    else:
        print("The book collection is NOT a valid binary search tree.")


if __name__ == "__main__":
    main()
