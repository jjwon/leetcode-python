# Decode Ways

[Link to the problem](https://leetcode.com/problems/decode-ways/)

## Problem Statement
A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message `"12"`, it could be decoded as `"AB"` (1 2) or `"L"` (12).

The number of ways decoding `"12"` is 2.

## Solution

To solve this problem, we'll use dynamic programming.

There are two base cases:
  - when our encoded message is of size 0, there is only one way to decode the message.
  - when our encoded message is of size 1, there is only one way to decode the message, unless it is `"0"`, in which there are no valid ways to decode the message.

For any other message size, we can decompose it into smaller subproblems as follows:

    decodeWays(m) = decodeWays(m[1:])
                          +
                    decodeWays(m[2:]) # if 1 <= int(m[:2]) <= 26

This is conditional on that `m[0] != "0"`.  Otherwise, it is a message with no valid decoding.

Therefore, we can solve this problem by iterating backwards over the string, and building up our library that way.

## Caveats

You might have noticed that in our solution, we have a corner case where we map `s=""` to `numDecodings = 0`.  This is to pass a corner case for LeetCode, which we think is poorly handled, considering that `""` could reasonably be decoded as `""`.
