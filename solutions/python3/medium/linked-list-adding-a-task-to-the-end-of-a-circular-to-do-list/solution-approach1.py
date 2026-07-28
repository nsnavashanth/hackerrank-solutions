# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/linked-list-adding-a-task-to-the-end-of-a-circular-to-do-list/problem?isFullScreen=true
# Problem     Linked List - Adding a Task to the End of a Circular To-Do List
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-28, 10:12 a.m.
# Technique   circular-linked-list-traversal
# Time        O(N^2)
# Space       O(N)
# Insight     The implementation maintains the circular property by ensuring the last node's next pointer always references the head node during every append operation.
# Interview   Before: "How would you append to a circular list?" After: "I traverse to the node where next is head, then update pointers. This takes O(N) per append, leading to O(N^2) total time for N insertions, which is acceptable given the constraints."
# Pitfalls    (1) Failing to update the new node's next pointer to the head, which breaks the circular structure.  (2) Using a standard linked list traversal that terminates at None, causing an infinite loop in a circular list.  (3) Neglecting the special case where the list is initially empty, which requires setting the head to the new node.
# ──────────────────────────────────────────────────

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def display(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break


n = int(input())
arr = list(map(int, input().split()))

cll = CircularLinkedList()

for x in arr:
    cll.append(x)

cll.display()
