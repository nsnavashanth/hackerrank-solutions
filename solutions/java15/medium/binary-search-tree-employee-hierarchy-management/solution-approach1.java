// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-search-tree-employee-hierarchy-management/problem?isFullScreen=true
// Problem     Binary Search Tree - Employee Hierarchy Management
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-07-31, 10:26 a.m.
// ──────────────────────────────────────────────────

import java.util.Scanner;

public class Solution {

    // Simple, clean inner class for Tree Nodes
    static class Node {
        int val;
        Node left;
        Node right;

        Node(int val) {
            this.val = val;
        }
    }

    // Iterative BST insertion to prevent StackOverflow on large/unbalanced trees
    public static Node insert(Node root, int val) {
        if (root == null) {
            return new Node(val);
        }

        var curr = root;
        while (true) {
            if (val < curr.val) {
                if (curr.left == null) {
                    curr.left = new Node(val);
                    break;
                }
                curr = curr.left;
            } else if (val > curr.val) {
                if (curr.right == null) {
                    curr.right = new Node(val);
                    break;
                }
                curr = curr.right;
            } else {
                // Ignore duplicates if present
                break;
            }
        }
        return root;
            }

    // O(H) Lowest Common Ancestor search using BST properties
    public static int findLCA(Node root, int p, int q) {
        var curr = root;
        while (curr != null) {
            // Both values are strictly smaller -> move left
            if (p < curr.val && q < curr.val) {
                curr = curr.left;
            } 
            // Both values are strictly larger -> move right
            else if (p > curr.val && q > curr.val) {
                curr = curr.right;
            } 
            // Split point found: curr is the Lowest Common Ancestor
            else {
                return curr.val;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        // Fast and reliable token parsing across custom HackerRank inputs
        var scanner = new Scanner(System.in);

        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        Node root = null;

        for (int i = 0; i < n; i++) {
            int val = scanner.nextInt();
            root = insert(root, val);
        }

        int p = scanner.nextInt();
        int q = scanner.nextInt();

        // Compute and print the LCA
        System.out.println(findLCA(root, p, q));

        scanner.close();
    }
}
