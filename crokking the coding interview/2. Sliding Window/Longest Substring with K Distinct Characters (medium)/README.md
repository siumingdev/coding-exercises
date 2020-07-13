# Longest Substring with K Distinct Characters

## Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

## Naive Solution

Try all subarray. Number of subarray = $O(N^2)$, so time complexity is also $O(N^2)$.

## Better Solution

Implemented in `solution.py`. Time complexity = $O(N)$. Space complexity = $O(K)$.

Idea: Similar to previous one, just treat the substring as a subarray and use a hashmap to keep track of the counts of characters in current substring.