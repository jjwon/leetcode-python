# Maximum Gap

[Link to the problem](https://leetcode.com/problems/maximum-gap/)

## Problem Statement
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

## Solution

To solve this problem, we'll use bucket sort.

[Bucket sort](https://www.wikiwand.com/en/Bucket_sort) is a sorting algorithm that divides elements into a number of buckets.  When being used to sort an array, it runs in average-case *O(n+k)* time, where *k* is the number of buckets used.

We'll use bucket sort here with `len(nums)` buckets.  This ensures that either every bucket will have exactly one element (in which we now have a sorted list, and can simply iterate through it to find the gap), or there will be some empty buckets, which means that the largest gap will be around these buckets.  Now, we just iterate through the buckets, and compare the max element of the previous bucket with the min element of the next non-empty bucket.  By doing this, we'll end up finding the largest gap.
