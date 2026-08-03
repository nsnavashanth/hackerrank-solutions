// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/priority-queue-most-popular-products-in-an-online-store/problem?isFullScreen=true
// Problem     Priority Queue - Most Popular Products in an Online Store
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:45 p.m.
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int id = scanner.nextInt();
            freqMap.put(id, freqMap.getOrDefault(id, 0) + 1);
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int k = scanner.nextInt();

        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>(
            (a, b) -> {
                if (!a.getValue().equals(b.getValue())) {
                    return Integer.compare(b.getValue(), a.getValue());
                }
                return Integer.compare(b.getKey(), a.getKey());
            }
        );

        maxHeap.addAll(freqMap.entrySet());

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k && !maxHeap.isEmpty(); i++) {
            result.add(maxHeap.poll().getKey());
        }

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        System.out.println();

        scanner.close();
    }
}
