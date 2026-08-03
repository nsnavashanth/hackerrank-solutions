// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/ti27110-sri-sai-ram/challenges/binary-search-tree-efficient-book-search-in-a-digital-library/problem?isFullScreen=true
// Problem     Binary Search Tree - Efficient Book Search in a Digital Library
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-08-03, 10:39 p.m.
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

    private static TreeNode searchBST(TreeNode root, int val) {
        TreeNode curr = root;
        while (curr != null) {
            if (curr.val == val) {
                return curr;
            } else if (val < curr.val) {
                curr = curr.left;
            } else {
                curr = curr.right;
            }
        }
        return null;
    }

    private static void inorderTraversal(TreeNode root, List<Integer> result) {
        if (root != null) {
            inorderTraversal(root.left, result);
            result.add(root.val);
            inorderTraversal(root.right, result);
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
            int bookId = scanner.nextInt();
            root = insertIntoBST(root, bookId);
        }

        if (!scanner.hasNextInt()) {
            return;
        }
        int targetId = scanner.nextInt();

        TreeNode targetNode = searchBST(root, targetId);

        if (targetNode != null) {
            List<Integer> subtreeVals = new ArrayList<>();
            inorderTraversal(targetNode, subtreeVals);

            System.out.println("Book found! Subtree rooted at " + targetId + ":");
            for (int i = 0; i < subtreeVals.size(); i++) {
                System.out.print(subtreeVals.get(i) + (i == subtreeVals.size() - 1 ? "" : " "));
            }
            System.out.println();
        } else {
            System.out.print("Book not found");
        }

        scanner.close();
    }
}
