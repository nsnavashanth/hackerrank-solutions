// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/hashing-employee-salary-management-system/problem?isFullScreen=true
// Problem     Hashing - Employee Salary Management System
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:47 p.m.
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
        Map<Integer, Integer> salaryMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int empId = scanner.nextInt();
            int salary = scanner.nextInt();
            salaryMap.put(empId, salary);
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            int queryId = scanner.nextInt();
            if (salaryMap.containsKey(queryId)) {
                System.out.println(salaryMap.get(queryId));
            } else {
                System.out.println("Employee not found");
            }
        }

        scanner.close();
    }
}
