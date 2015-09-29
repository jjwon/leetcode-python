# Edit Distance

[Link to the problem](https://leetcode.com/problems/edit-distance/)

## Problem Statement
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character

## Solution

To solve this problem, we'll use dynamic programming, where we incrementally compare the edit distances of the substrings of `word1` and `word2`.

There are two base cases:
  - when we compare a substring of `word1` with an empty `word2`, the edit distance is `len(word1)` (we need that many deletions)
  - when we compare an empty `word1` with a substring of `word2`, the edit distance is `len(word2)` (we need that many insertions)

For any other message size, we can decompose it into smaller subproblems as follows:

    editDistance(i, j) = min(
                    editDistance(i-1, j-1), # if word1[i-1] == word2[j-1]
                    editDistance(i-1, j) + 1, # deletion
                    editDistance(i, j-1) + 1, # insertion
                    editDistance(i-1, j-1) + 1, # substitution

Therefore, we can solve this problem by filling out the dynamic programming matrix iteratively.  The time complexity and space complexity will both be O(mn).

For a more thorough treatment of edit distance, take a look at the [Needleman-Wunsch algorithm](https://www.wikiwand.com/en/Needleman%E2%80%93Wunsch_algorithm), which considers more complex scoring methods (such as a gap penalty).
