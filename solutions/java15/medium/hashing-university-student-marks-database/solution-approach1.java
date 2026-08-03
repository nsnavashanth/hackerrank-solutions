// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/hashing-university-student-marks-database/problem?isFullScreen=true
// Problem     Hashing - University Student Marks Database
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:48 p.m.
// ──────────────────────────────────────────────────

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        Map<Integer, Integer> studentMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int studentId = scanner.nextInt();
            int marks = scanner.nextInt();
            studentMap.put(studentId, marks);
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            int queryId = scanner.nextInt();
            if (studentMap.containsKey(queryId)) {
                System.out.println(studentMap.get(queryId));
            } else {
                System.out.println("Student not found");
            }
        }

        scanner.close();
    }
}
