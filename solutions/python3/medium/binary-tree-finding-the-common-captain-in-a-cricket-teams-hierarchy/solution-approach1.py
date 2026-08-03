# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-tree-finding-the-common-captain-in-a-cricket-teams-hierarchy/problem?isFullScreen=true
# Problem     Binary Tree - Finding the Common Captain in a Cricket Team's Hierarchy
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:11 a.m.
# ──────────────────────────────────────────────────

import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(nodes_input):
    if not nodes_input or nodes_input[0] == "null":
        return None

    root = Node(int(nodes_input[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(nodes_input):
        current = queue.popleft()

        # Left child
        if i < len(nodes_input):
            if nodes_input[i] != "null":
                current.left = Node(int(nodes_input[i]))
                queue.append(current.left)
            i += 1

        # Right child
        if i < len(nodes_input):
            if nodes_input[i] != "null":
                current.right = Node(int(nodes_input[i]))
                queue.append(current.right)
            i += 1

    return root

def find_lca(root, p, q):
    if root is None or root.val == p or root.val == q:
        return root

    left_lca = find_lca(root.left, p, q)
    right_lca = find_lca(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

def main():
    input_data = sys.stdin.read().split()
    if not input_data or len(input_data) < 3:
        return

    # Extract p and q from the very end of the input stream
    q = int(input_data[-1])
    p = int(input_data[-2])
    
    # Everything in between index 1 and -2 is the tree level-order representation
    nodes_input = input_data[1:-2]

    root = build_tree(nodes_input)
    lca_node = find_lca(root, p, q)
    
    if lca_node:
        print(lca_node.val)

if __name__ == "__main__":
    main()
