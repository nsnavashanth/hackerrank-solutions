# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/queue-ticket-booking-system/problem?isFullScreen=true
# Problem     Queue - Ticket Booking System
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-29, 10:30 a.m.
# Technique   list-based-queue
# Time        O(N) per dequeue
# Space       O(K)
# Insight     The implementation maintains a first-in-first-out order by utilizing the list's pop(0) method to remove the oldest element while enforcing a fixed capacity constraint during enqueue operations.
# Interview   Before: "I will use a standard list to manage the queue." After: "I implemented a queue using a list with O(N) dequeue operations due to shifting elements, ensuring the capacity constraint is checked before every enqueue to prevent overflow."
# Pitfalls    (1) Using pop(0) on a Python list results in O(N) time complexity, which may be inefficient for large queues.  (2) Failing to handle the specific output format for empty queues as required by the problem statement.  (3) Neglecting the capacity limit check before appending new elements to the queue.
# ──────────────────────────────────────────────────

class TicketQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, name):
        if len(self.queue) >= self.capacity:
            print(f"Queue is full. Cannot add {name}")
        else:
            self.queue.append(name)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Served Customer: Queue is empty. No customer to serve.")
        else:
            served = self.queue.pop(0)
            print(f"Served Customer: {served}")

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print(f"Current Queue: {' '.join(self.queue)}")


if __name__ == "__main__":
    capacity = int(input().strip())
    ticket_system = TicketQueue(capacity)
    
    n_ops = int(input().strip())
    
    for _ in range(n_ops):
        line = input().strip().split()
        if not line:
            continue
            
        command = line[0]
        
        if command == "ENQUEUE":
            name = " ".join(line[1:])
            ticket_system.enqueue(name)
        elif command == "DEQUEUE":
            ticket_system.dequeue()
        elif command == "DISPLAY":
            ticket_system.display()
