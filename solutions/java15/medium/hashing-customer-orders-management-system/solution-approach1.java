// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/hashing-customer-orders-management-system/problem?isFullScreen=true
// Problem     Hashing - Customer Orders Management System
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:46 p.m.
// ──────────────────────────────────────────────────

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        String[] directAddressTable = new String[1001];

        for (int i = 0; i < n; i++) {
            int orderId = scanner.nextInt();
            String customerName = scanner.next();
            if (orderId >= 0 && orderId <= 1000) {
                directAddressTable[orderId] = customerName;
            }
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            int queryId = scanner.nextInt();
            if (queryId >= 0 && queryId <= 1000 && directAddressTable[queryId] != null) {
                System.out.println(directAddressTable[queryId]);
            } else {
                System.out.println("Order not found");
            }
        }

        scanner.close();
    }
}
