# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-tree-library-book-collection-tracker/problem?isFullScreen=true
# Problem     Binary Tree - Library Book Collection Tracker
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 09:11 a.m.
# Technique   level-order-queue-insertion
# Time        O(n)
# Space       O(n)
# Insight     The implementation uses a queue to maintain level-order insertion, ensuring each node is processed exactly once to build the tree and subsequently counted via a recursive traversal.
# Interview   Before: "How would you build a binary tree from a list and count its nodes?" After: "I used a queue to perform level-order insertion, which runs in O(n) time and space, followed by a recursive O(n) traversal to count the nodes, correctly handling the n input size."
# Pitfalls    (1) Failing to handle the empty input case where n is zero, which would cause an index error if not checked.  (2) Incorrectly assuming the tree is a binary search tree, whereas the problem specifies a standard binary tree structure built level-by-level.  (3) Mismanaging the queue pointer index i, which must be incremented after each child insertion to avoid skipping elements.
# ──────────────────────────────────────────────────

import sys
from collections import deque

class Node:
    """Represents a node (book) in the Binary Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Class to manage Binary Tree operations."""
    def __init__(self):
        self.root = None

    def insert_level_order(self, book_ids):
        """Inserts book IDs into the binary tree level by level."""
        if not book_ids:
            return

        self.root = Node(book_ids[0])
        queue = deque([self.root])
        i = 1

        while i < len(book_ids):
            current = queue.popleft()

            # Insert left child
            if i < len(book_ids):
                current.left = Node(book_ids[i])
                queue.append(current.left)
                i += 1

            # Insert right child
            if i < len(book_ids):
                current.right = Node(book_ids[i])
                queue.append(current.right)
                i += 1

    def count_nodes(self, node):
        """Recursively counts the total number of nodes in the binary tree."""
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


def main():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    book_ids = [int(x) for x in input_data[1:n+1]]

    tree = BinaryTree()
    tree.insert_level_order(book_ids)

    # Count nodes using the recursive method
    total_books = tree.count_nodes(tree.root)
    print(total_books)

if __name__ == "__main__":
    main()
