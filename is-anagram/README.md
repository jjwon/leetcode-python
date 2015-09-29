# Decode Ways

## Problem Statement
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

## Solution
There are three ways essential ways to solve this problem: 1) sorting, 2) counting, 3) prime hashing.

### Solution 1: Sorting
We sort string s and t and compare if their sorted versions are equal. If N is the total length of both strings, then this solution is O(N) in time and O(N) space.


### Solution 2: Counting
We create a dictionary of character counts for each string s and t. For example, for a string like "leet" would have a python dictionary that looks like this:

	{"l": 1,
	 "e": 2,
	 "t":1
	}


### Solution 3: Prime Hashing
This is my personal favorite. We are given that the string contains only lowercase letters so we can take advantage of this and combine it with Solution 2. For every letter, "a", "b", ..."z", we map it to a prime number, 2, 3,...101 (the first 26 prime numbers). 

Every anagram will be represented as a product of these primes. We essentially treat each anagram as a prime factorization. This "hashcode" will ignore the order of the characters which is exactly what we want.

If N is the total length of both strings, then this solution is O(N) in time and O(1) space.



## Caveats
If you actually ran the solutions you'll notice that the fastest solutions, in order of decreasing speed, are:

1. Solution 1: 94 ms
2. Solution 2: 104 ms
3. Solution 3: 1288 ms

Basically, it's due to two things:

1. Python's sort methods are heavily optimized and are much faster than the list comprehensions used in Solution 3
2. leetcode insantiates a Solution object for every test case so the import statements contribute significant overhead. For example, we noticed that if you move the all of the import statments and precomputed dictionary into the SolutionThree.hash function, the overall speed remained the same.

