// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/priority-queue-ayushi-and-the-magical-chocolate-piles/problem?isFullScreen=true
// Problem     Priority Queue - Ayushi and the Magical Chocolate Piles
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:43 p.m.
// ──────────────────────────────────────────────────

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        PriorityQueue<Long> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            maxHeap.add(scanner.nextLong());
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int k = scanner.nextInt();

        for (int i = 0; i < k; i++) {
            if (maxHeap.isEmpty()) {
                break;
            }
            long maxPile = maxHeap.poll();
            long remaining = (long) Math.sqrt(maxPile);
            maxHeap.add(remaining);
        }

        long totalChocolates = 0;
        while (!maxHeap.isEmpty()) {
            totalChocolates += maxHeap.poll();
        }

        System.out.println(totalChocolates);

        scanner.close();
    }
}
