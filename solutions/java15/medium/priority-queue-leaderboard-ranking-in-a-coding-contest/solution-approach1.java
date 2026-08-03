// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/priority-queue-leaderboard-ranking-in-a-coding-contest/problem?isFullScreen=true
// Problem     Priority Queue - Leaderboard Ranking in a Coding Contest
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:44 p.m.
// ──────────────────────────────────────────────────

import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        String[] scores = new String[n];

        for (int i = 0; i < n; i++) {
            scores[i] = scanner.next();
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int k = scanner.nextInt();

        Arrays.sort(scores, (a, b) -> {
            if (a.length() != b.length()) {
                return Integer.compare(a.length(), b.length());
            }
            return a.compareTo(b);
        });

        System.out.println(scores[n - k]);

        scanner.close();
    }
}
