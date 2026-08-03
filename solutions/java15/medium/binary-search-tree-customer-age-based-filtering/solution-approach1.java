// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-search-tree-customer-age-based-filtering/problem?isFullScreen=true
// Problem     Binary Search Tree - Customer Age-Based Filtering
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:42 p.m.
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Solution {

    private static TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else if (val > root.val) {
            root.right = insertIntoBST(root.right, val);
        }
        return root;
    }

    private static TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) {
            return null;
        }

        if (root.val < low) {
            return trimBST(root.right, low, high);
        }
        if (root.val > high) {
            return trimBST(root.left, low, high);
        }

        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);

        return root;
    }

    private static void preorderTraversal(TreeNode root, List<Integer> result) {
        if (root != null) {
            result.add(root.val);
            preorderTraversal(root.left, result);
            preorderTraversal(root.right, result);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            return;
        }

        int n = scanner.nextInt();
        TreeNode root = null;

        for (int i = 0; i < n; i++) {
            int age = scanner.nextInt();
            root = insertIntoBST(root, age);
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int low = scanner.nextInt();

        if (!scanner.hasNextInt()) {
            return;
        }
        int high = scanner.nextInt();

        root = trimBST(root, low, high);

        List<Integer> result = new ArrayList<>();
        preorderTraversal(root, result);

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        System.out.println();

        scanner.close();
    }
}
