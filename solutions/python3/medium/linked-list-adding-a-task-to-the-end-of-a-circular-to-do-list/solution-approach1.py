# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/linked-list-adding-a-task-to-the-end-of-a-circular-to-do-list/problem?isFullScreen=true
# Problem     Linked List - Adding a Task to the End of a Circular To-Do List
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-28, 10:10 a.m.
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
