# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-search-tree-organizing-a-library-collection/problem?isFullScreen=true
# Problem     Binary Search Tree - Organizing a Library Collection
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:37 p.m.
# ──────────────────────────────────────────────────

import sys


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)

    return root


def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    book_ids = [int(x) for x in input_data[1 : n + 1]]

    root = None
    for book_id in book_ids:
        root = insert_into_bst(root, book_id)

    result = []
    inorder_traversal(root, result)

    print(*(result))


if __name__ == "__main__":
    main()
