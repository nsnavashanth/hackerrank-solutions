// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/priority-queue-reordering-packages-in-a-delivery-center/problem?isFullScreen=true
// Problem     Priority Queue - Reordering Packages in a Delivery Center
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:44 p.m.
// ──────────────────────────────────────────────────

import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int k = scanner.nextInt();

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        int index = 0;
        for (int i = 0; i <= k && i < n; i++) {
            minHeap.add(arr[i]);
        }

        for (int i = k + 1; i < n; i++) {
            arr[index++] = minHeap.poll();
            minHeap.add(arr[i]);
        }

        while (!minHeap.isEmpty()) {
            arr[index++] = minHeap.poll();
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + (i == n - 1 ? "" : " "));
        }
        System.out.println();

        scanner.close();
    }
}
