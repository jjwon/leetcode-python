# Letter Combinations of a Phone Number

[Link to the problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem Statement
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![image](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

**Note**:

Although the above answer is in lexicographical order, your answer could be in any order you want.

## Solution

To solve this problem, we'll use depth-first search, using the call-stack to manage our recursion.

We'll keep track of an *intermediate*, the list that we'll be modifying to keep track of a particular letter combination, and a set of *results*, which is the number of complete letter combinations we've seen thus far.  At a certain stage, we can grab the next digit, append a potential letter, and recurse.  However, we must remember to remove this letter after the recursion completes so we can proceed with other potential letters at this stage.
