# Number of 1 Bits

[Link to the problem](https://leetcode.com/problems/number-of-1-bits/)

## Problem Statement

Write a function that takes an unsigned integer and returns the number of `1` bits it has (also known as the Hamming weight).

For example, the 32-bit integer `11` has binary representation `00000000000000000000000000001011`, so the function should return 3.

## Solution

We simply iterate over all 32 bits, checking whether the ith bit is active using bit operations.  We can check if `(1 << i) & n` is nonzero to verify whether the nth bit is on; `1 << i` will be the number with just the ith bit turned on.
