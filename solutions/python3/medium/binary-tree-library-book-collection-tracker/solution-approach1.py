# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-tree-library-book-collection-tracker/problem?isFullScreen=true
# Problem     Binary Tree - Library Book Collection Tracker
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 09:11 a.m.
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
