# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-tree-cricket-team-hierarchy-visualization/problem?isFullScreen=true
# Problem     Binary Tree - Cricket Team Hierarchy Visualization
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:35 p.m.
# ──────────────────────────────────────────────────

from collections import deque
import sys


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes):
    if not nodes or nodes[0] == "null":
        return None

    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        curr = queue.popleft()

        if i < len(nodes) and nodes[i] != "null":
            curr.left = TreeNode(int(nodes[i]))
            queue.append(curr.left)
        i += 1

        if i < len(nodes) and nodes[i] != "null":
            curr.right = TreeNode(int(nodes[i]))
            queue.append(curr.right)
        i += 1

    return root


def right_side_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    nodes = input_data[1:]

    root = build_tree(nodes)
    visible_members = right_side_view(root)

    print(*(visible_members))


if __name__ == "__main__":
    main()
