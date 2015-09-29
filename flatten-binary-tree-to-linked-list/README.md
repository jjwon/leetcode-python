# Flatten Binary Tree to Linked List

[Link to the problem](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Problem Statement
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

## Solution

We simply perform a pre-order traversal of the tree, and flatten the tree recursively at every step.  Afterwards, we arrange the nodes onto the right side of the tree.
