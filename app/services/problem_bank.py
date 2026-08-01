"""Curated coding problem bank for deterministic LeetCode-style questions.

Contains 50 problems across 10 categories:
  - Arrays & Hashing (7)
  - Two Pointers (5)
  - Sliding Window (4)
  - Stack & Queue (4)
  - Binary Search (4)
  - Linked Lists (5)
  - Trees & Graphs (7)
  - Dynamic Programming (6)
  - Strings (5)
  - Design (3)

Each problem has public + hidden test cases, function signatures,
and starter code generation for multiple languages.
"""

from __future__ import annotations

import random
import re
from typing import Any

from app.services.topic_taxonomy import topic_matches_problem


PROBLEM_BANK: list[dict[str, Any]] = [
    # ═══════════════════════════════════════════════════════════════════
    # ARRAYS & HASHING
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Two Sum",
        "difficulty": "easy",
        "topics": ["array", "hashmap", "two sum"],
        "statement": (
            "Given an integer array nums and an integer target, return indices of the two numbers "
            "such that they add up to target. You may assume exactly one valid answer exists, "
            "and you may not use the same element twice."
        ),
        "constraints": [
            "2 <= nums.length <= 10^4",
            "-10^9 <= nums[i] <= 10^9",
            "-10^9 <= target <= 10^9",
            "Exactly one valid answer exists.",
        ],
        "examples": [
            {"input": "nums = [2, 7, 11, 15], target = 9", "output": "[0, 1]", "explanation": "nums[0] + nums[1] == 9"},
            {"input": "nums = [3, 2, 4], target = 6", "output": "[1, 2]"},
        ],
        "public_test_cases": [
            {"input": "[2,7,11,15], 9", "expected_output": "[0,1]"},
            {"input": "[3,2,4], 6", "expected_output": "[1,2]"},
            {"input": "[3,3], 6", "expected_output": "[0,1]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["array", "hash table"],
        "function_name": "two_sum",
        "params": ["nums", "target"],
    },
    {
        "title": "Contains Duplicate",
        "difficulty": "easy",
        "topics": ["array", "hashmap", "set"],
        "statement": (
            "Given an integer array nums, return true if any value appears at least twice "
            "in the array, and return false if every element is distinct."
        ),
        "constraints": [
            "1 <= nums.length <= 10^5",
            "-10^9 <= nums[i] <= 10^9",
        ],
        "examples": [
            {"input": "nums = [1, 2, 3, 1]", "output": "true"},
            {"input": "nums = [1, 2, 3, 4]", "output": "false"},
        ],
        "public_test_cases": [
            {"input": "[1,2,3,1]", "expected_output": "true"},
            {"input": "[1,2,3,4]", "expected_output": "false"},
            {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "true"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["array", "hash table"],
        "function_name": "contains_duplicate",
        "params": ["nums"],
    },
    {
        "title": "Product of Array Except Self",
        "difficulty": "medium",
        "topics": ["array", "prefix-sum"],
        "statement": (
            "Given an integer array nums, return an array answer such that answer[i] is equal to "
            "the product of all the elements of nums except nums[i]. You must solve it in O(n) "
            "time without using the division operation."
        ),
        "constraints": [
            "2 <= nums.length <= 10^5",
            "-30 <= nums[i] <= 30",
            "The product of any prefix or suffix fits in a 32-bit integer.",
        ],
        "examples": [
            {"input": "nums = [1, 2, 3, 4]", "output": "[24, 12, 8, 6]"},
            {"input": "nums = [-1, 1, 0, -3, 3]", "output": "[0, 0, 9, 0, 0]"},
        ],
        "public_test_cases": [
            {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]"},
            {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1) (output array not counted)",
        "tags": ["array", "prefix sum"],
        "function_name": "product_except_self",
        "params": ["nums"],
    },
    {
        "title": "Top K Frequent Elements",
        "difficulty": "medium",
        "topics": ["array", "hashmap", "sorting", "heap"],
        "statement": (
            "Given an integer array nums and an integer k, return the k most frequent elements. "
            "You may return the answer in any order."
        ),
        "constraints": [
            "1 <= nums.length <= 10^5",
            "-10^4 <= nums[i] <= 10^4",
            "k is in the range [1, number of unique elements].",
            "The answer is guaranteed to be unique.",
        ],
        "examples": [
            {"input": "nums = [1,1,1,2,2,3], k = 2", "output": "[1, 2]"},
            {"input": "nums = [1], k = 1", "output": "[1]"},
        ],
        "public_test_cases": [
            {"input": "[1,1,1,2,2,3], 2", "expected_output": "[1,2]"},
            {"input": "[1], 1", "expected_output": "[1]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["array", "hash table", "heap"],
        "function_name": "top_k_frequent",
        "params": ["nums", "k"],
    },
    {
        "title": "Encode and Decode Strings",
        "difficulty": "medium",
        "topics": ["array", "string", "design"],
        "statement": (
            "Design an algorithm to encode a list of strings to a single string. "
            "The encoded string is then decoded back to the original list of strings. "
            "Implement encode and decode functions."
        ),
        "constraints": [
            "0 <= strs.length <= 200",
            "0 <= strs[i].length <= 200",
            "strs[i] contains any possible characters including delimiters.",
        ],
        "examples": [
            {"input": 'strs = ["hello", "world"]', "output": '["hello", "world"]'},
        ],
        "public_test_cases": [
            {"input": '["hello","world"]', "expected_output": '["hello","world"]'},
            {"input": '[""]', "expected_output": '[""]'},
        ],
        "expected_time_complexity": "O(n) where n is total chars",
        "expected_space_complexity": "O(1) extra",
        "tags": ["array", "string", "design"],
        "function_name": "encode_decode",
        "params": ["strs"],
    },
    {
        "title": "Longest Consecutive Sequence",
        "difficulty": "hard",
        "topics": ["array", "hashmap", "union-find"],
        "statement": (
            "Given an unsorted array of integers nums, return the length of the longest "
            "consecutive elements sequence. You must write an algorithm that runs in O(n) time."
        ),
        "constraints": [
            "0 <= nums.length <= 10^5",
            "-10^9 <= nums[i] <= 10^9",
        ],
        "examples": [
            {"input": "nums = [100, 4, 200, 1, 3, 2]", "output": "4", "explanation": "The sequence is [1, 2, 3, 4]."},
            {"input": "nums = [0,3,7,2,5,8,4,6,0,1]", "output": "9"},
        ],
        "public_test_cases": [
            {"input": "[100,4,200,1,3,2]", "expected_output": "4"},
            {"input": "[0,3,7,2,5,8,4,6,0,1]", "expected_output": "9"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["array", "hash table", "union find"],
        "function_name": "longest_consecutive",
        "params": ["nums"],
    },
    {
        "title": "Group Anagrams",
        "difficulty": "medium",
        "topics": ["hashmap", "string", "sorting"],
        "statement": (
            "Given an array of strings strs, group the anagrams together. "
            "You can return the answer in any order."
        ),
        "constraints": [
            "1 <= strs.length <= 10^4",
            "0 <= strs[i].length <= 100",
            "strs[i] consists of lowercase English letters.",
        ],
        "examples": [
            {
                "input": 'strs = ["eat","tea","tan","ate","nat","bat"]',
                "output": '[["bat"],["nat","tan"],["ate","eat","tea"]]',
            }
        ],
        "public_test_cases": [
            {"input": '["eat","tea","tan","ate","nat","bat"]', "expected_output": '[["bat"],["nat","tan"],["ate","eat","tea"]]'},
            {"input": '[""]', "expected_output": '[[""]]'},
        ],
        "expected_time_complexity": "O(n * k log k)",
        "expected_space_complexity": "O(n * k)",
        "tags": ["hash table", "string", "sorting"],
        "function_name": "group_anagrams",
        "params": ["strs"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # TWO POINTERS
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Valid Palindrome",
        "difficulty": "easy",
        "topics": ["two-pointer", "string"],
        "statement": (
            "Given a string s, return true if it is a palindrome after converting all uppercase "
            "letters to lowercase and removing all non-alphanumeric characters."
        ),
        "constraints": [
            "1 <= s.length <= 2 * 10^5",
            "s consists of printable ASCII characters.",
        ],
        "examples": [
            {"input": 's = "A man, a plan, a canal: Panama"', "output": "true"},
            {"input": 's = "race a car"', "output": "false"},
        ],
        "public_test_cases": [
            {"input": '"A man, a plan, a canal: Panama"', "expected_output": "true"},
            {"input": '"race a car"', "expected_output": "false"},
            {"input": '" "', "expected_output": "true"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["two pointers", "string"],
        "function_name": "is_palindrome",
        "params": ["s"],
    },
    {
        "title": "Two Sum II - Input Array Is Sorted",
        "difficulty": "easy",
        "topics": ["two-pointer", "array", "binary-search"],
        "statement": (
            "Given a 1-indexed sorted integer array numbers, find two numbers that add up to target. "
            "Return their indices as [index1, index2] where 1 <= index1 < index2 <= numbers.length."
        ),
        "constraints": [
            "2 <= numbers.length <= 3 * 10^4",
            "-1000 <= numbers[i] <= 1000",
            "numbers is sorted in non-decreasing order.",
            "Exactly one solution exists.",
        ],
        "examples": [
            {"input": "numbers = [2,7,11,15], target = 9", "output": "[1, 2]"},
        ],
        "public_test_cases": [
            {"input": "[2,7,11,15], 9", "expected_output": "[1,2]"},
            {"input": "[2,3,4], 6", "expected_output": "[1,3]"},
            {"input": "[-1,0], -1", "expected_output": "[1,2]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["two pointers", "array", "binary search"],
        "function_name": "two_sum_sorted",
        "params": ["numbers", "target"],
    },
    {
        "title": "3Sum",
        "difficulty": "medium",
        "topics": ["two-pointer", "array", "sorting"],
        "statement": (
            "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] "
            "such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0. "
            "The solution set must not contain duplicate triplets."
        ),
        "constraints": [
            "3 <= nums.length <= 3000",
            "-10^5 <= nums[i] <= 10^5",
        ],
        "examples": [
            {"input": "nums = [-1, 0, 1, 2, -1, -4]", "output": "[[-1, -1, 2], [-1, 0, 1]]"},
        ],
        "public_test_cases": [
            {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]"},
            {"input": "[0,1,1]", "expected_output": "[]"},
            {"input": "[0,0,0]", "expected_output": "[[0,0,0]]"},
        ],
        "expected_time_complexity": "O(n^2)",
        "expected_space_complexity": "O(1) (not counting output)",
        "tags": ["two pointers", "array", "sorting"],
        "function_name": "three_sum",
        "params": ["nums"],
    },
    {
        "title": "Container With Most Water",
        "difficulty": "medium",
        "topics": ["two-pointer", "array", "greedy"],
        "statement": (
            "Given an integer array height of length n, find two lines that together with the x-axis "
            "form a container that holds the most water. Return the maximum amount of water."
        ),
        "constraints": [
            "n == height.length",
            "2 <= n <= 10^5",
            "0 <= height[i] <= 10^4",
        ],
        "examples": [
            {"input": "height = [1,8,6,2,5,4,8,3,7]", "output": "49"},
        ],
        "public_test_cases": [
            {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49"},
            {"input": "[1,1]", "expected_output": "1"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["two pointers", "array", "greedy"],
        "function_name": "max_area",
        "params": ["height"],
    },
    {
        "title": "Trapping Rain Water",
        "difficulty": "hard",
        "topics": ["two-pointer", "array", "stack", "dynamic-programming"],
        "statement": (
            "Given n non-negative integers representing an elevation map where the width of each "
            "bar is 1, compute how much water it can trap after raining."
        ),
        "constraints": [
            "n == height.length",
            "1 <= n <= 2 * 10^4",
            "0 <= height[i] <= 10^5",
        ],
        "examples": [
            {"input": "height = [0,1,0,2,1,0,1,3,2,1,2,1]", "output": "6"},
            {"input": "height = [4,2,0,3,2,5]", "output": "9"},
        ],
        "public_test_cases": [
            {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6"},
            {"input": "[4,2,0,3,2,5]", "expected_output": "9"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["two pointers", "array", "stack", "dynamic programming"],
        "function_name": "trap",
        "params": ["height"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # SLIDING WINDOW
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "easy",
        "topics": ["sliding-window", "array", "greedy"],
        "statement": (
            "Given an array prices where prices[i] is the price of a stock on the ith day, "
            "return the maximum profit you can achieve from one buy and one sell. "
            "If no profit is possible, return 0."
        ),
        "constraints": [
            "1 <= prices.length <= 10^5",
            "0 <= prices[i] <= 10^4",
        ],
        "examples": [
            {"input": "prices = [7,1,5,3,6,4]", "output": "5", "explanation": "Buy on day 2, sell on day 5."},
            {"input": "prices = [7,6,4,3,1]", "output": "0"},
        ],
        "public_test_cases": [
            {"input": "[7,1,5,3,6,4]", "expected_output": "5"},
            {"input": "[7,6,4,3,1]", "expected_output": "0"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["array", "dynamic programming"],
        "function_name": "max_profit",
        "params": ["prices"],
    },
    {
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "medium",
        "topics": ["sliding window", "string", "hashmap"],
        "statement": (
            "Given a string s, find the length of the longest substring without repeating characters."
        ),
        "constraints": [
            "0 <= s.length <= 5 * 10^4",
            "s consists of English letters, digits, symbols and spaces.",
        ],
        "examples": [
            {"input": 's = "abcabcbb"', "output": "3", "explanation": '"abc"'},
            {"input": 's = "bbbbb"', "output": "1"},
        ],
        "public_test_cases": [
            {"input": '"abcabcbb"', "expected_output": "3"},
            {"input": '"bbbbb"', "expected_output": "1"},
            {"input": '"pwwkew"', "expected_output": "3"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(min(n, alphabet))",
        "tags": ["string", "sliding window"],
        "function_name": "length_of_longest_substring",
        "params": ["s"],
    },
    {
        "title": "Longest Repeating Character Replacement",
        "difficulty": "medium",
        "topics": ["sliding-window", "string"],
        "statement": (
            "Given a string s and an integer k, you can choose any character and change it "
            "to any other uppercase English character at most k times. Return the length of "
            "the longest substring containing the same letter after performing at most k changes."
        ),
        "constraints": [
            "1 <= s.length <= 10^5",
            "s consists of only uppercase English letters.",
            "0 <= k <= s.length",
        ],
        "examples": [
            {"input": 's = "ABAB", k = 2', "output": "4"},
            {"input": 's = "AABABBA", k = 1', "output": "4"},
        ],
        "public_test_cases": [
            {"input": '"ABAB", 2', "expected_output": "4"},
            {"input": '"AABABBA", 1', "expected_output": "4"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1) (26 letters)",
        "tags": ["string", "sliding window"],
        "function_name": "character_replacement",
        "params": ["s", "k"],
    },
    {
        "title": "Minimum Window Substring",
        "difficulty": "hard",
        "topics": ["sliding-window", "string", "hashmap"],
        "statement": (
            "Given two strings s and t, return the minimum window substring of s such that "
            "every character in t (including duplicates) is included. If there is no such "
            "substring, return the empty string."
        ),
        "constraints": [
            "1 <= s.length, t.length <= 10^5",
            "s and t consist of uppercase and lowercase English letters.",
        ],
        "examples": [
            {"input": 's = "ADOBECODEBANC", t = "ABC"', "output": '"BANC"'},
        ],
        "public_test_cases": [
            {"input": '"ADOBECODEBANC", "ABC"', "expected_output": '"BANC"'},
            {"input": '"a", "a"', "expected_output": '"a"'},
            {"input": '"a", "aa"', "expected_output": '""'},
        ],
        "expected_time_complexity": "O(|s| + |t|)",
        "expected_space_complexity": "O(|s| + |t|)",
        "tags": ["string", "sliding window", "hash table"],
        "function_name": "min_window",
        "params": ["s", "t"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # STACK & QUEUE
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Valid Parentheses",
        "difficulty": "easy",
        "topics": ["stack", "string", "parentheses"],
        "statement": (
            "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', "
            "determine if the input string is valid. A string is valid if open brackets are closed "
            "by the same type of brackets and in the correct order."
        ),
        "constraints": [
            "1 <= s.length <= 10^4",
            "s consists of parentheses only: ()[]{}",
        ],
        "examples": [
            {"input": 's = "()[]{}"', "output": "true"},
            {"input": 's = "(]"', "output": "false"},
        ],
        "public_test_cases": [
            {"input": '"()"', "expected_output": "true"},
            {"input": '"()[]{}"', "expected_output": "true"},
            {"input": '"(]"', "expected_output": "false"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["stack", "string"],
        "function_name": "is_valid",
        "params": ["s"],
    },
    {
        "title": "Min Stack",
        "difficulty": "medium",
        "topics": ["stack", "design"],
        "statement": (
            "Design a stack that supports push, pop, top, and retrieving the minimum element "
            "in constant time. Implement push(val), pop(), top(), and getMin()."
        ),
        "constraints": [
            "-2^31 <= val <= 2^31 - 1",
            "pop, top, and getMin will always be called on non-empty stacks.",
            "At most 3 * 10^4 calls will be made.",
        ],
        "examples": [
            {
                "input": "push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()",
                "output": "[-3, 0, -2]",
            },
        ],
        "public_test_cases": [
            {"input": "push(-2),push(0),push(-3),getMin(),pop(),top(),getMin()", "expected_output": "[-3,0,-2]"},
        ],
        "expected_time_complexity": "O(1) per operation",
        "expected_space_complexity": "O(n)",
        "tags": ["stack", "design"],
        "function_name": "min_stack",
        "params": ["operations"],
    },
    {
        "title": "Daily Temperatures",
        "difficulty": "medium",
        "topics": ["stack", "monotonic stack", "array"],
        "statement": (
            "Given an array of integers temperatures representing daily temperatures, "
            "return an array answer such that answer[i] is the number of days you have to wait "
            "after the ith day to get a warmer temperature. If there is no future day with a "
            "warmer temperature, answer[i] == 0."
        ),
        "constraints": [
            "1 <= temperatures.length <= 10^5",
            "30 <= temperatures[i] <= 100",
        ],
        "examples": [
            {"input": "temperatures = [73,74,75,71,69,72,76,73]", "output": "[1,1,4,2,1,1,0,0]"},
        ],
        "public_test_cases": [
            {"input": "[73,74,75,71,69,72,76,73]", "expected_output": "[1,1,4,2,1,1,0,0]"},
            {"input": "[30,40,50,60]", "expected_output": "[1,1,1,0]"},
            {"input": "[30,60,90]", "expected_output": "[1,1,0]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["stack", "monotonic stack", "array"],
        "function_name": "daily_temperatures",
        "params": ["temperatures"],
    },
    {
        "title": "Largest Rectangle in Histogram",
        "difficulty": "hard",
        "topics": ["stack", "monotonic stack", "array"],
        "statement": (
            "Given an array of integers heights representing the histogram's bar heights "
            "where the width of each bar is 1, return the area of the largest rectangle "
            "in the histogram."
        ),
        "constraints": [
            "1 <= heights.length <= 10^5",
            "0 <= heights[i] <= 10^4",
        ],
        "examples": [
            {"input": "heights = [2,1,5,6,2,3]", "output": "10"},
            {"input": "heights = [2,4]", "output": "4"},
        ],
        "public_test_cases": [
            {"input": "[2,1,5,6,2,3]", "expected_output": "10"},
            {"input": "[2,4]", "expected_output": "4"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["stack", "monotonic stack", "array"],
        "function_name": "largest_rectangle_area",
        "params": ["heights"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # BINARY SEARCH
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Binary Search",
        "difficulty": "easy",
        "topics": ["binary-search", "array"],
        "statement": (
            "Given a sorted array of integers nums and a target value, return the index if "
            "the target is found. If not, return -1."
        ),
        "constraints": [
            "1 <= nums.length <= 10^4",
            "-10^4 < nums[i], target < 10^4",
            "All integers in nums are unique.",
            "nums is sorted in ascending order.",
        ],
        "examples": [
            {"input": "nums = [-1,0,3,5,9,12], target = 9", "output": "4"},
            {"input": "nums = [-1,0,3,5,9,12], target = 2", "output": "-1"},
        ],
        "public_test_cases": [
            {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4"},
            {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1"},
        ],
        "expected_time_complexity": "O(log n)",
        "expected_space_complexity": "O(1)",
        "tags": ["binary search", "array"],
        "function_name": "search",
        "params": ["nums", "target"],
    },
    {
        "title": "Search in Rotated Sorted Array",
        "difficulty": "medium",
        "topics": ["binary-search", "array"],
        "statement": (
            "Given a rotated sorted array nums and a target, return the index of target if it "
            "is in nums, or -1 if not. You must write an algorithm with O(log n) runtime."
        ),
        "constraints": [
            "1 <= nums.length <= 5000",
            "-10^4 <= nums[i] <= 10^4",
            "All values in nums are unique.",
            "nums was rotated at some pivot unknown to you beforehand.",
        ],
        "examples": [
            {"input": "nums = [4,5,6,7,0,1,2], target = 0", "output": "4"},
            {"input": "nums = [4,5,6,7,0,1,2], target = 3", "output": "-1"},
        ],
        "public_test_cases": [
            {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4"},
            {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1"},
            {"input": "[1], 0", "expected_output": "-1"},
        ],
        "expected_time_complexity": "O(log n)",
        "expected_space_complexity": "O(1)",
        "tags": ["binary search", "array"],
        "function_name": "search_rotated",
        "params": ["nums", "target"],
    },
    {
        "title": "Find Minimum in Rotated Sorted Array",
        "difficulty": "medium",
        "topics": ["binary-search", "array"],
        "statement": (
            "Given a sorted rotated array nums of unique elements, return the minimum element. "
            "You must write an algorithm that runs in O(log n) time."
        ),
        "constraints": [
            "n == nums.length",
            "1 <= n <= 5000",
            "-5000 <= nums[i] <= 5000",
            "All integers are unique.",
        ],
        "examples": [
            {"input": "nums = [3,4,5,1,2]", "output": "1"},
            {"input": "nums = [4,5,6,7,0,1,2]", "output": "0"},
        ],
        "public_test_cases": [
            {"input": "[3,4,5,1,2]", "expected_output": "1"},
            {"input": "[4,5,6,7,0,1,2]", "expected_output": "0"},
            {"input": "[11,13,15,17]", "expected_output": "11"},
        ],
        "expected_time_complexity": "O(log n)",
        "expected_space_complexity": "O(1)",
        "tags": ["binary search", "array"],
        "function_name": "find_min",
        "params": ["nums"],
    },
    {
        "title": "Median of Two Sorted Arrays",
        "difficulty": "hard",
        "topics": ["binary-search", "array"],
        "statement": (
            "Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays. "
            "The overall run time complexity should be O(log(m + n))."
        ),
        "constraints": [
            "nums1.length == m, nums2.length == n",
            "0 <= m, n <= 1000",
            "1 <= m + n <= 2000",
            "-10^6 <= nums1[i], nums2[i] <= 10^6",
        ],
        "examples": [
            {"input": "nums1 = [1,3], nums2 = [2]", "output": "2.0"},
            {"input": "nums1 = [1,2], nums2 = [3,4]", "output": "2.5"},
        ],
        "public_test_cases": [
            {"input": "[1,3], [2]", "expected_output": "2.0"},
            {"input": "[1,2], [3,4]", "expected_output": "2.5"},
        ],
        "expected_time_complexity": "O(log(m + n))",
        "expected_space_complexity": "O(1)",
        "tags": ["binary search", "array", "divide and conquer"],
        "function_name": "find_median_sorted_arrays",
        "params": ["nums1", "nums2"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # LINKED LISTS
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Reverse Linked List",
        "difficulty": "easy",
        "topics": ["linked-list"],
        "statement": "Given the head of a singly linked list, reverse the list and return the reversed list.",
        "constraints": [
            "The number of nodes is in the range [0, 5000].",
            "-5000 <= Node.val <= 5000",
        ],
        "examples": [
            {"input": "head = [1,2,3,4,5]", "output": "[5,4,3,2,1]"},
            {"input": "head = [1,2]", "output": "[2,1]"},
        ],
        "public_test_cases": [
            {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]"},
            {"input": "[1,2]", "expected_output": "[2,1]"},
            {"input": "[]", "expected_output": "[]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["linked list"],
        "function_name": "reverse_list",
        "params": ["head"],
    },
    {
        "title": "Linked List Cycle",
        "difficulty": "easy",
        "topics": ["linked-list", "two-pointer"],
        "statement": (
            "Given head, the head of a linked list, determine if the linked list has a cycle. "
            "Return true if there is a cycle, false otherwise."
        ),
        "constraints": [
            "The number of nodes is in the range [0, 10^4].",
            "-10^5 <= Node.val <= 10^5",
        ],
        "examples": [
            {"input": "head = [3,2,0,-4], pos = 1", "output": "true"},
            {"input": "head = [1], pos = -1", "output": "false"},
        ],
        "public_test_cases": [
            {"input": "[3,2,0,-4], 1", "expected_output": "true"},
            {"input": "[1], -1", "expected_output": "false"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["linked list", "two pointers"],
        "function_name": "has_cycle",
        "params": ["head"],
    },
    {
        "title": "Merge Two Sorted Lists",
        "difficulty": "easy",
        "topics": ["linked-list", "recursion"],
        "statement": (
            "Merge two sorted linked lists into one sorted list by splicing together the nodes. "
            "Return the head of the merged list."
        ),
        "constraints": [
            "Both lists are sorted in non-decreasing order.",
            "The number of nodes in both lists is in the range [0, 50].",
        ],
        "examples": [
            {"input": "list1 = [1,2,4], list2 = [1,3,4]", "output": "[1,1,2,3,4,4]"},
        ],
        "public_test_cases": [
            {"input": "[1,2,4], [1,3,4]", "expected_output": "[1,1,2,3,4,4]"},
            {"input": "[], []", "expected_output": "[]"},
            {"input": "[], [0]", "expected_output": "[0]"},
        ],
        "expected_time_complexity": "O(n + m)",
        "expected_space_complexity": "O(1)",
        "tags": ["linked list", "recursion"],
        "function_name": "merge_two_lists",
        "params": ["list1", "list2"],
    },
    {
        "title": "Reorder List",
        "difficulty": "medium",
        "topics": ["linked-list", "two-pointer"],
        "statement": (
            "Given the head of a singly linked list L0 → L1 → … → Ln-1 → Ln, reorder it to: "
            "L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … You may not modify the values, only nodes."
        ),
        "constraints": [
            "The number of nodes is in the range [1, 5 * 10^4].",
            "1 <= Node.val <= 1000",
        ],
        "examples": [
            {"input": "head = [1,2,3,4]", "output": "[1,4,2,3]"},
            {"input": "head = [1,2,3,4,5]", "output": "[1,5,2,4,3]"},
        ],
        "public_test_cases": [
            {"input": "[1,2,3,4]", "expected_output": "[1,4,2,3]"},
            {"input": "[1,2,3,4,5]", "expected_output": "[1,5,2,4,3]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["linked list", "two pointers", "stack"],
        "function_name": "reorder_list",
        "params": ["head"],
    },
    {
        "title": "Merge K Sorted Lists",
        "difficulty": "hard",
        "topics": ["linked-list", "heap", "divide-and-conquer"],
        "statement": (
            "Given an array of k linked lists, each sorted in ascending order, "
            "merge all the linked lists into one sorted linked list and return it."
        ),
        "constraints": [
            "k == lists.length",
            "0 <= k <= 10^4",
            "0 <= lists[i].length <= 500",
            "-10^4 <= lists[i][j] <= 10^4",
            "Total nodes across all lists <= 10^4.",
        ],
        "examples": [
            {"input": "lists = [[1,4,5],[1,3,4],[2,6]]", "output": "[1,1,2,3,4,4,5,6]"},
        ],
        "public_test_cases": [
            {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]"},
            {"input": "[]", "expected_output": "[]"},
            {"input": "[[]]", "expected_output": "[]"},
        ],
        "expected_time_complexity": "O(N log k)",
        "expected_space_complexity": "O(k)",
        "tags": ["linked list", "heap", "divide and conquer"],
        "function_name": "merge_k_lists",
        "params": ["lists"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # TREES & GRAPHS
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Invert Binary Tree",
        "difficulty": "easy",
        "topics": ["trees", "dfs", "bfs"],
        "statement": "Given the root of a binary tree, invert the tree and return its root.",
        "constraints": [
            "The number of nodes is in the range [0, 100].",
            "-100 <= Node.val <= 100",
        ],
        "examples": [
            {"input": "root = [4,2,7,1,3,6,9]", "output": "[4,7,2,9,6,3,1]"},
        ],
        "public_test_cases": [
            {"input": "[4,2,7,1,3,6,9]", "expected_output": "[4,7,2,9,6,3,1]"},
            {"input": "[2,1,3]", "expected_output": "[2,3,1]"},
            {"input": "[]", "expected_output": "[]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(h) where h is height",
        "tags": ["tree", "dfs", "bfs"],
        "function_name": "invert_tree",
        "params": ["root"],
    },
    {
        "title": "Maximum Depth of Binary Tree",
        "difficulty": "easy",
        "topics": ["trees", "dfs", "bfs"],
        "statement": "Given the root of a binary tree, return its maximum depth (number of nodes along the longest path from root to farthest leaf).",
        "constraints": [
            "The number of nodes is in the range [0, 10^4].",
            "-100 <= Node.val <= 100",
        ],
        "examples": [
            {"input": "root = [3,9,20,null,null,15,7]", "output": "3"},
        ],
        "public_test_cases": [
            {"input": "[3,9,20,null,null,15,7]", "expected_output": "3"},
            {"input": "[1,null,2]", "expected_output": "2"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(h)",
        "tags": ["tree", "dfs", "bfs"],
        "function_name": "max_depth",
        "params": ["root"],
    },
    {
        "title": "Validate Binary Search Tree",
        "difficulty": "medium",
        "topics": ["trees", "bst", "dfs"],
        "statement": (
            "Given the root of a binary tree, determine if it is a valid binary search tree (BST). "
            "A valid BST has left subtree values less than root and right subtree values greater."
        ),
        "constraints": [
            "The number of nodes is in the range [1, 10^4].",
            "-2^31 <= Node.val <= 2^31 - 1",
        ],
        "examples": [
            {"input": "root = [2,1,3]", "output": "true"},
            {"input": "root = [5,1,4,null,null,3,6]", "output": "false"},
        ],
        "public_test_cases": [
            {"input": "[2,1,3]", "expected_output": "true"},
            {"input": "[5,1,4,null,null,3,6]", "expected_output": "false"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["tree", "dfs", "bst"],
        "function_name": "is_valid_bst",
        "params": ["root"],
    },
    {
        "title": "Lowest Common Ancestor of a BST",
        "difficulty": "medium",
        "topics": ["trees", "bst"],
        "statement": (
            "Given a binary search tree (BST) and two nodes p and q, find their lowest common ancestor (LCA). "
            "The LCA is the lowest node that has both p and q as descendants."
        ),
        "constraints": [
            "All node values are unique.",
            "p != q",
            "p and q will exist in the BST.",
        ],
        "examples": [
            {"input": "root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8", "output": "6"},
        ],
        "public_test_cases": [
            {"input": "[6,2,8,0,4,7,9,null,null,3,5], 2, 8", "expected_output": "6"},
            {"input": "[6,2,8,0,4,7,9,null,null,3,5], 2, 4", "expected_output": "2"},
        ],
        "expected_time_complexity": "O(h)",
        "expected_space_complexity": "O(1)",
        "tags": ["tree", "bst"],
        "function_name": "lowest_common_ancestor",
        "params": ["root", "p", "q"],
    },
    {
        "title": "Level Order Traversal",
        "difficulty": "medium",
        "topics": ["trees", "bfs", "queue"],
        "statement": (
            "Given the root of a binary tree, return the level order traversal of its nodes' values "
            "(i.e., from left to right, level by level)."
        ),
        "constraints": [
            "The number of nodes is in the range [0, 2000].",
            "-1000 <= Node.val <= 1000",
        ],
        "examples": [
            {"input": "root = [3,9,20,null,null,15,7]", "output": "[[3],[9,20],[15,7]]"},
        ],
        "public_test_cases": [
            {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]"},
            {"input": "[1]", "expected_output": "[[1]]"},
            {"input": "[]", "expected_output": "[]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["tree", "bfs"],
        "function_name": "level_order",
        "params": ["root"],
    },
    {
        "title": "Number of Islands",
        "difficulty": "medium",
        "topics": ["graphs", "dfs", "bfs", "matrix"],
        "statement": (
            "Given an m x n 2D grid of '1's (land) and '0's (water), return the number of islands. "
            "An island is surrounded by water and formed by connecting adjacent lands horizontally "
            "or vertically."
        ),
        "constraints": [
            "m == grid.length",
            "n == grid[i].length",
            "1 <= m, n <= 300",
            "grid[i][j] is '0' or '1'.",
        ],
        "examples": [
            {"input": 'grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]', "output": "3"},
        ],
        "public_test_cases": [
            {"input": '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]', "expected_output": "1"},
            {"input": '[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]', "expected_output": "3"},
        ],
        "expected_time_complexity": "O(m * n)",
        "expected_space_complexity": "O(m * n) worst case",
        "tags": ["graph", "dfs", "bfs", "matrix"],
        "function_name": "num_islands",
        "params": ["grid"],
    },
    {
        "title": "Word Ladder",
        "difficulty": "hard",
        "topics": ["graphs", "bfs"],
        "statement": (
            "Given two words beginWord and endWord, and a dictionary wordList, return the "
            "number of words in the shortest transformation sequence from beginWord to endWord, "
            "where only one letter can be changed at a time and each intermediate word must "
            "exist in wordList. Return 0 if no such sequence exists."
        ),
        "constraints": [
            "1 <= beginWord.length <= 10",
            "endWord.length == beginWord.length",
            "1 <= wordList.length <= 5000",
            "All words have the same length.",
            "All words consist of lowercase English letters.",
        ],
        "examples": [
            {"input": 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]', "output": "5"},
        ],
        "public_test_cases": [
            {"input": '"hit", "cog", ["hot","dot","dog","lot","log","cog"]', "expected_output": "5"},
            {"input": '"hit", "cog", ["hot","dot","dog","lot","log"]', "expected_output": "0"},
        ],
        "expected_time_complexity": "O(M^2 * N) where M = word length, N = list size",
        "expected_space_complexity": "O(M^2 * N)",
        "tags": ["graph", "bfs"],
        "function_name": "ladder_length",
        "params": ["begin_word", "end_word", "word_list"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # DYNAMIC PROGRAMMING
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Climbing Stairs",
        "difficulty": "easy",
        "topics": ["dynamic-programming", "math"],
        "statement": (
            "You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. "
            "In how many distinct ways can you climb to the top?"
        ),
        "constraints": ["1 <= n <= 45"],
        "examples": [
            {"input": "n = 2", "output": "2", "explanation": "1+1 or 2"},
            {"input": "n = 3", "output": "3"},
        ],
        "public_test_cases": [
            {"input": "2", "expected_output": "2"},
            {"input": "3", "expected_output": "3"},
            {"input": "5", "expected_output": "8"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["dynamic programming", "math"],
        "function_name": "climb_stairs",
        "params": ["n"],
    },
    {
        "title": "Coin Change",
        "difficulty": "medium",
        "topics": ["dynamic-programming", "bfs"],
        "statement": (
            "Given an integer array coins representing coin denominations and an integer amount, "
            "return the fewest number of coins needed to make up that amount. Return -1 if "
            "that amount cannot be made up by any combination."
        ),
        "constraints": [
            "1 <= coins.length <= 12",
            "1 <= coins[i] <= 2^31 - 1",
            "0 <= amount <= 10^4",
        ],
        "examples": [
            {"input": "coins = [1,5,10,25], amount = 30", "output": "2"},
            {"input": "coins = [2], amount = 3", "output": "-1"},
        ],
        "public_test_cases": [
            {"input": "[1,5,10,25], 30", "expected_output": "2"},
            {"input": "[2], 3", "expected_output": "-1"},
            {"input": "[1], 0", "expected_output": "0"},
        ],
        "expected_time_complexity": "O(amount * n)",
        "expected_space_complexity": "O(amount)",
        "tags": ["dynamic programming", "bfs"],
        "function_name": "coin_change",
        "params": ["coins", "amount"],
    },
    {
        "title": "Longest Increasing Subsequence",
        "difficulty": "medium",
        "topics": ["dynamic-programming", "binary-search"],
        "statement": (
            "Given an integer array nums, return the length of the longest strictly increasing "
            "subsequence."
        ),
        "constraints": [
            "1 <= nums.length <= 2500",
            "-10^4 <= nums[i] <= 10^4",
        ],
        "examples": [
            {"input": "nums = [10,9,2,5,3,7,101,18]", "output": "4", "explanation": "[2,3,7,101]"},
            {"input": "nums = [0,1,0,3,2,3]", "output": "4"},
        ],
        "public_test_cases": [
            {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4"},
            {"input": "[0,1,0,3,2,3]", "expected_output": "4"},
            {"input": "[7,7,7,7,7,7,7]", "expected_output": "1"},
        ],
        "expected_time_complexity": "O(n log n)",
        "expected_space_complexity": "O(n)",
        "tags": ["dynamic programming", "binary search"],
        "function_name": "length_of_lis",
        "params": ["nums"],
    },
    {
        "title": "House Robber",
        "difficulty": "medium",
        "topics": ["dynamic-programming"],
        "statement": (
            "Given an integer array nums representing money at each house arranged in a line, "
            "determine the maximum amount you can rob without robbing two adjacent houses."
        ),
        "constraints": [
            "1 <= nums.length <= 100",
            "0 <= nums[i] <= 400",
        ],
        "examples": [
            {"input": "nums = [1,2,3,1]", "output": "4", "explanation": "Rob houses 1 and 3."},
            {"input": "nums = [2,7,9,3,1]", "output": "12"},
        ],
        "public_test_cases": [
            {"input": "[1,2,3,1]", "expected_output": "4"},
            {"input": "[2,7,9,3,1]", "expected_output": "12"},
            {"input": "[2,1,1,2]", "expected_output": "4"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["dynamic programming"],
        "function_name": "rob",
        "params": ["nums"],
    },
    {
        "title": "Unique Paths",
        "difficulty": "medium",
        "topics": ["dynamic-programming", "math"],
        "statement": (
            "A robot is located at the top-left corner of an m x n grid. The robot can only "
            "move right or down. How many unique paths are there to reach the bottom-right corner?"
        ),
        "constraints": [
            "1 <= m, n <= 100",
        ],
        "examples": [
            {"input": "m = 3, n = 7", "output": "28"},
            {"input": "m = 3, n = 2", "output": "3"},
        ],
        "public_test_cases": [
            {"input": "3, 7", "expected_output": "28"},
            {"input": "3, 2", "expected_output": "3"},
            {"input": "1, 1", "expected_output": "1"},
        ],
        "expected_time_complexity": "O(m * n)",
        "expected_space_complexity": "O(n)",
        "tags": ["dynamic programming", "math"],
        "function_name": "unique_paths",
        "params": ["m", "n"],
    },
    {
        "title": "Edit Distance",
        "difficulty": "hard",
        "topics": ["dynamic-programming", "string"],
        "statement": (
            "Given two strings word1 and word2, return the minimum number of operations "
            "required to convert word1 to word2. You have three operations: insert, delete, "
            "or replace a character."
        ),
        "constraints": [
            "0 <= word1.length, word2.length <= 500",
            "word1 and word2 consist of lowercase English letters.",
        ],
        "examples": [
            {"input": 'word1 = "horse", word2 = "ros"', "output": "3"},
            {"input": 'word1 = "intention", word2 = "execution"', "output": "5"},
        ],
        "public_test_cases": [
            {"input": '"horse", "ros"', "expected_output": "3"},
            {"input": '"intention", "execution"', "expected_output": "5"},
        ],
        "expected_time_complexity": "O(m * n)",
        "expected_space_complexity": "O(m * n)",
        "tags": ["dynamic programming", "string"],
        "function_name": "min_distance",
        "params": ["word1", "word2"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # STRINGS
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Valid Anagram",
        "difficulty": "easy",
        "topics": ["string", "hashmap", "sorting"],
        "statement": (
            "Given two strings s and t, return true if t is an anagram of s, and false otherwise. "
            "An anagram uses all original letters exactly once."
        ),
        "constraints": [
            "1 <= s.length, t.length <= 5 * 10^4",
            "s and t consist of lowercase English letters.",
        ],
        "examples": [
            {"input": 's = "anagram", t = "nagaram"', "output": "true"},
            {"input": 's = "rat", t = "car"', "output": "false"},
        ],
        "public_test_cases": [
            {"input": '"anagram", "nagaram"', "expected_output": "true"},
            {"input": '"rat", "car"', "expected_output": "false"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1) (26 letters)",
        "tags": ["string", "hash table", "sorting"],
        "function_name": "is_anagram",
        "params": ["s", "t"],
    },
    {
        "title": "Longest Palindromic Substring",
        "difficulty": "medium",
        "topics": ["string", "dynamic-programming"],
        "statement": "Given a string s, return the longest palindromic substring in s.",
        "constraints": [
            "1 <= s.length <= 1000",
            "s consists of only digits and English letters.",
        ],
        "examples": [
            {"input": 's = "babad"', "output": '"bab"', "explanation": '"aba" is also valid.'},
            {"input": 's = "cbbd"', "output": '"bb"'},
        ],
        "public_test_cases": [
            {"input": '"babad"', "expected_output": '"bab"'},
            {"input": '"cbbd"', "expected_output": '"bb"'},
        ],
        "expected_time_complexity": "O(n^2)",
        "expected_space_complexity": "O(1)",
        "tags": ["string", "dynamic programming"],
        "function_name": "longest_palindrome",
        "params": ["s"],
    },
    {
        "title": "Count and Say",
        "difficulty": "medium",
        "topics": ["string", "recursion"],
        "statement": (
            "The count-and-say sequence is a sequence of digit strings defined by the recursive formula: "
            "countAndSay(1) = '1', countAndSay(n) is the run-length encoding of countAndSay(n - 1). "
            "Given a positive integer n, return the nth element of the sequence."
        ),
        "constraints": ["1 <= n <= 30"],
        "examples": [
            {"input": "n = 4", "output": '"1211"', "explanation": '1 → 11 → 21 → 1211'},
        ],
        "public_test_cases": [
            {"input": "1", "expected_output": '"1"'},
            {"input": "4", "expected_output": '"1211"'},
        ],
        "expected_time_complexity": "O(2^n) worst case",
        "expected_space_complexity": "O(2^n)",
        "tags": ["string"],
        "function_name": "count_and_say",
        "params": ["n"],
    },
    {
        "title": "String to Integer (atoi)",
        "difficulty": "medium",
        "topics": ["string", "math"],
        "statement": (
            "Implement the myAtoi function, which converts a string to a 32-bit signed integer. "
            "The algorithm: ignore leading whitespace, read optional sign, read digits until "
            "non-digit or end, clamp to [-2^31, 2^31 - 1]."
        ),
        "constraints": [
            "0 <= s.length <= 200",
            "s consists of English letters, digits, ' ', '+', '-', '.'",
        ],
        "examples": [
            {"input": 's = "42"', "output": "42"},
            {"input": 's = "   -42"', "output": "-42"},
            {"input": 's = "4193 with words"', "output": "4193"},
        ],
        "public_test_cases": [
            {"input": '"42"', "expected_output": "42"},
            {"input": '"   -42"', "expected_output": "-42"},
            {"input": '"4193 with words"', "expected_output": "4193"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(1)",
        "tags": ["string", "math"],
        "function_name": "my_atoi",
        "params": ["s"],
    },
    {
        "title": "Palindrome Partitioning",
        "difficulty": "hard",
        "topics": ["string", "backtracking", "dynamic-programming"],
        "statement": (
            "Given a string s, partition s such that every substring of the partition is a palindrome. "
            "Return all possible palindrome partitionings of s."
        ),
        "constraints": [
            "1 <= s.length <= 16",
            "s contains only lowercase English letters.",
        ],
        "examples": [
            {"input": 's = "aab"', "output": '[["a","a","b"],["aa","b"]]'},
        ],
        "public_test_cases": [
            {"input": '"aab"', "expected_output": '[["a","a","b"],["aa","b"]]'},
            {"input": '"a"', "expected_output": '[["a"]]'},
        ],
        "expected_time_complexity": "O(n * 2^n)",
        "expected_space_complexity": "O(n)",
        "tags": ["string", "backtracking", "dynamic programming"],
        "function_name": "partition",
        "params": ["s"],
    },

    # ═══════════════════════════════════════════════════════════════════
    # DESIGN
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Merge Intervals",
        "difficulty": "medium",
        "topics": ["intervals", "sorting"],
        "statement": (
            "Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping "
            "intervals and return an array of non-overlapping intervals that cover all the intervals."
        ),
        "constraints": [
            "1 <= intervals.length <= 10^4",
            "intervals[i].length == 2",
            "0 <= start_i <= end_i <= 10^4",
        ],
        "examples": [
            {"input": "[[1,3],[2,6],[8,10],[15,18]]", "output": "[[1,6],[8,10],[15,18]]"},
            {"input": "[[1,4],[4,5]]", "output": "[[1,5]]"},
        ],
        "public_test_cases": [
            {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]"},
            {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]"},
        ],
        "expected_time_complexity": "O(n log n)",
        "expected_space_complexity": "O(n)",
        "tags": ["array", "sorting"],
        "function_name": "merge",
        "params": ["intervals"],
    },
    {
        "title": "LRU Cache",
        "difficulty": "hard",
        "topics": ["design", "hashmap", "linked list"],
        "statement": (
            "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. "
            "Implement the LRUCache class with get(key) and put(key, value), both in O(1) average time."
        ),
        "constraints": [
            "1 <= capacity <= 3000",
            "0 <= key <= 10^4",
            "0 <= value <= 10^5",
            "At most 2 * 10^5 calls to get and put.",
        ],
        "examples": [
            {
                "input": "LRUCache(2), put(1,1), put(2,2), get(1), put(3,3), get(2)",
                "output": "[null,null,null,1,null,-1]",
            }
        ],
        "public_test_cases": [
            {
                "input": "capacity=2; operations=put(1,1), put(2,2), get(1), put(3,3), get(2)",
                "expected_output": "[1,-1]",
            }
        ],
        "expected_time_complexity": "O(1) average per operation",
        "expected_space_complexity": "O(capacity)",
        "tags": ["design", "hash table", "linked list"],
        "function_name": "lru_cache",
        "params": ["operations"],
    },
    {
        "title": "Serialize and Deserialize Binary Tree",
        "difficulty": "hard",
        "topics": ["design", "trees", "dfs", "bfs"],
        "statement": (
            "Design an algorithm to serialize and deserialize a binary tree. Serialization is "
            "converting a tree to a string; deserialization is reconstructing the tree from the string."
        ),
        "constraints": [
            "The number of nodes is in the range [0, 10^4].",
            "-1000 <= Node.val <= 1000",
        ],
        "examples": [
            {"input": "root = [1,2,3,null,null,4,5]", "output": "[1,2,3,null,null,4,5]"},
        ],
        "public_test_cases": [
            {"input": "[1,2,3,null,null,4,5]", "expected_output": "[1,2,3,null,null,4,5]"},
            {"input": "[]", "expected_output": "[]"},
        ],
        "expected_time_complexity": "O(n)",
        "expected_space_complexity": "O(n)",
        "tags": ["design", "tree", "dfs", "bfs"],
        "function_name": "serialize_deserialize",
        "params": ["root"],
    },
]


# ═══════════════════════════════════════════════════════════════════════
# HIDDEN TEST CASES (for objective scoring)
# ═══════════════════════════════════════════════════════════════════════

_HIDDEN_TESTS_BY_PROBLEM_ID: dict[str, list[dict[str, str]]] = {
    "two-sum": [
        {"input": "[1,5,3,7], 8", "expected_output": "[0,3]"},
        {"input": "[-3,4,3,90], 0", "expected_output": "[0,2]"},
        {"input": "[0,4,3,0], 0", "expected_output": "[0,3]"},
    ],
    "contains-duplicate": [
        {"input": "[1,2,3,4,5]", "expected_output": "false"},
        {"input": "[1]", "expected_output": "false"},
        {"input": "[1,2,1]", "expected_output": "true"},
    ],
    "product-of-array-except-self": [
        {"input": "[2,3,4,5]", "expected_output": "[60,40,30,24]"},
        {"input": "[1,0,3]", "expected_output": "[0,3,0]"},
    ],
    "top-k-frequent-elements": [
        {"input": "[1,1,2,2,3], 2", "expected_output": "[1,2]"},
        {"input": "[4,4,4,1,1,2], 2", "expected_output": "[4,1]"},
    ],
    "longest-consecutive-sequence": [
        {"input": "[1,2,0,1]", "expected_output": "3"},
        {"input": "[]", "expected_output": "0"},
        {"input": "[9,1,4,7,3,-1,0,5,8,-1,6]", "expected_output": "7"},
    ],
    "group-anagrams": [
        {"input": '["abc","bca","cab","foo","ofo"]', "expected_output": '[["abc","bca","cab"],["foo","ofo"]]'},
        {"input": '["a"]', "expected_output": '[["a"]]'},
    ],
    "valid-palindrome": [
        {"input": '".,,"', "expected_output": "true"},
        {"input": '"ab"', "expected_output": "false"},
    ],
    "two-sum-ii-input-array-is-sorted": [
        {"input": "[1,2,3,4,4,9,56,90], 8", "expected_output": "[4,5]"},
    ],
    "3sum": [
        {"input": "[0,0,0,0]", "expected_output": "[[0,0,0]]"},
        {"input": "[-2,0,1,1,2]", "expected_output": "[[-2,0,2],[-2,1,1]]"},
    ],
    "container-with-most-water": [
        {"input": "[1,2,1]", "expected_output": "2"},
        {"input": "[4,3,2,1,4]", "expected_output": "16"},
    ],
    "trapping-rain-water": [
        {"input": "[1,0,1]", "expected_output": "1"},
        {"input": "[2,0,2]", "expected_output": "2"},
    ],
    "valid-parentheses": [
        {"input": '"([{}])"', "expected_output": "true"},
        {"input": '"([)]"', "expected_output": "false"},
        {"input": '""', "expected_output": "true"},
    ],
    "daily-temperatures": [
        {"input": "[89,62,70,58,47,47,46,76,100,70]", "expected_output": "[8,1,5,4,3,2,1,1,0,0]"},
    ],
    "largest-rectangle-in-histogram": [
        {"input": "[1]", "expected_output": "1"},
        {"input": "[2,1,2]", "expected_output": "3"},
    ],
    "binary-search": [
        {"input": "[5], 5", "expected_output": "0"},
        {"input": "[2,5], 5", "expected_output": "1"},
    ],
    "search-in-rotated-sorted-array": [
        {"input": "[3,1], 1", "expected_output": "1"},
        {"input": "[5,1,3], 5", "expected_output": "0"},
    ],
    "find-minimum-in-rotated-sorted-array": [
        {"input": "[2,1]", "expected_output": "1"},
        {"input": "[1]", "expected_output": "1"},
    ],
    "median-of-two-sorted-arrays": [
        {"input": "[1], [2,3]", "expected_output": "2.0"},
        {"input": "[], [1]", "expected_output": "1.0"},
    ],
    "reverse-linked-list": [
        {"input": "[1]", "expected_output": "[1]"},
        {"input": "[1,2,3]", "expected_output": "[3,2,1]"},
    ],
    "merge-two-sorted-lists": [
        {"input": "[1,3,5], [2,4,6]", "expected_output": "[1,2,3,4,5,6]"},
    ],
    "merge-k-sorted-lists": [
        {"input": "[[1,2],[3,4],[0,5]]", "expected_output": "[0,1,2,3,4,5]"},
    ],
    "longest-substring-without-repeating-characters": [
        {"input": '""', "expected_output": "0"},
        {"input": '"dvdf"', "expected_output": "3"},
    ],
    "minimum-window-substring": [
        {"input": '"aa", "aa"', "expected_output": '"aa"'},
    ],
    "best-time-to-buy-and-sell-stock": [
        {"input": "[2,4,1]", "expected_output": "2"},
        {"input": "[1]", "expected_output": "0"},
    ],
    "climbing-stairs": [
        {"input": "1", "expected_output": "1"},
        {"input": "10", "expected_output": "89"},
    ],
    "coin-change": [
        {"input": "[1,2,5], 11", "expected_output": "3"},
        {"input": "[2], 1", "expected_output": "-1"},
    ],
    "longest-increasing-subsequence": [
        {"input": "[1,3,6,7,9,4,10,5,6]", "expected_output": "6"},
    ],
    "house-robber": [
        {"input": "[1]", "expected_output": "1"},
        {"input": "[1,2]", "expected_output": "2"},
    ],
    "unique-paths": [
        {"input": "7, 3", "expected_output": "28"},
        {"input": "3, 3", "expected_output": "6"},
    ],
    "edit-distance": [
        {"input": '"", "abc"', "expected_output": "3"},
        {"input": '"abc", ""', "expected_output": "3"},
    ],
    "valid-anagram": [
        {"input": '"ab", "a"', "expected_output": "false"},
        {"input": '"aab", "baa"', "expected_output": "true"},
    ],
    "longest-palindromic-substring": [
        {"input": '"a"', "expected_output": '"a"'},
        {"input": '"ac"', "expected_output": '"a"'},
    ],
    "merge-intervals": [
        {"input": "[[1,4],[0,2],[3,5]]", "expected_output": "[[0,5]]"},
        {"input": "[[1,4],[5,6]]", "expected_output": "[[1,4],[5,6]]"},
    ],
    "lru-cache": [
        {
            "input": "capacity=2; operations=put(2,1), put(2,2), get(2), put(1,1), put(4,1), get(2)",
            "expected_output": "[2,-1]",
        }
    ],
    "number-of-islands": [
        {"input": '[["1"]]', "expected_output": "1"},
        {"input": '[["0","0"],["0","0"]]', "expected_output": "0"},
    ],
    "validate-binary-search-tree": [
        {"input": "[1]", "expected_output": "true"},
    ],
    "level-order-traversal": [
        {"input": "[1,2,3,4,5]", "expected_output": "[[1],[2,3],[4,5]]"},
    ],
    "invert-binary-tree": [
        {"input": "[1,2]", "expected_output": "[1,null,2]"},
    ],
    "palindrome-partitioning": [
        {"input": '"aba"', "expected_output": '[["a","b","a"],["aba"]]'},
    ],
}


# ═══════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

def _problem_id_from_title(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.strip().lower()).strip("-")
    return slug or "coding-problem"


def get_problem_hidden_tests(problem_id: str | None) -> list[dict[str, str]]:
    if not problem_id:
        return []
    return list(_HIDDEN_TESTS_BY_PROBLEM_ID.get(problem_id, []))


def _language_starter_code(function_name: str, params: list[str], language: str) -> tuple[str, str]:
    joined = ", ".join(params)

    if language in {"python", "py"}:
        signature = f"def {function_name}({joined}):"
        starter = f"{signature}\n    # Write your solution\n    pass\n"
        return signature, starter

    if language in {"javascript", "js"}:
        signature = f"function {function_name}({joined}) {{"
        starter = f"{signature}\n  // Write your solution\n}}\n"
        return signature, starter

    if language in {"typescript", "ts"}:
        signature = f"function {function_name}({joined}: any): any {{"
        starter = f"{signature}\n  // Write your solution\n}}\n"
        return signature, starter

    if language == "java":
        signature = f"public static Object {function_name}({', '.join('Object ' + p for p in params)})"
        starter = (
            "class Solution {\n"
            f"    {signature} {{\n"
            "        // Write your solution\n"
            "        return null;\n"
            "    }\n"
            "}\n"
        )
        return signature, starter

    signature = f"{function_name}({joined})"
    starter = f"// Implement {signature}\n"
    return signature, starter


def _normalize_language(language: str | None) -> str:
    value = (language or "python").strip().lower()
    if value in {"py"}:
        return "python"
    if value in {"js"}:
        return "javascript"
    if value in {"ts"}:
        return "typescript"
    if value in {"golang"}:
        return "go"
    if value in {"c#"}:
        return "csharp"
    if value in {"c++"}:
        return "cpp"
    return value


def pick_coding_problem(
    *,
    difficulty: str,
    topic: str,
    programming_language: str | None,
    previous_questions: list[str] | None = None,
) -> dict[str, Any] | None:
    """Pick a curated coding problem close to requested topic and difficulty.

    This is the synchronous fallback used when no DB session is available.
    For the full hybrid flow (DB cache → static bank → AI), use
    ``async_pick_coding_problem()`` instead.
    """

    previous_l = "\n".join(previous_questions or []).lower()
    difficulty_l = difficulty.strip().lower()
    language = _normalize_language(programming_language)

    pool = [
        p
        for p in PROBLEM_BANK
        if p["difficulty"] == difficulty_l
        and topic_matches_problem(p, topic)
        and p["title"].lower() not in previous_l
    ]

    if not pool:
        pool = [
            p
            for p in PROBLEM_BANK
            if p["difficulty"] == difficulty_l and p["title"].lower() not in previous_l
        ]

    if not pool:
        pool = [p for p in PROBLEM_BANK if p["title"].lower() not in previous_l]

    if not pool:
        return None

    problem = random.choice(pool).copy()
    problem_id = _problem_id_from_title(problem["title"])
    signature, starter = _language_starter_code(
        problem["function_name"],
        problem["params"],
        language,
    )

    return {
        "title": problem["title"],
        "problem_id": problem_id,
        "statement": problem["statement"],
        "difficulty": problem["difficulty"],
        "constraints": list(problem["constraints"]),
        "examples": list(problem["examples"]),
        "function_name": problem["function_name"],
        "params": list(problem["params"]),
        "function_signature": signature,
        "starter_code": starter,
        "public_test_cases": list(problem["public_test_cases"]),
        "tags": list(problem["tags"]),
        "expected_time_complexity": problem["expected_time_complexity"],
        "expected_space_complexity": problem["expected_space_complexity"],
        "programming_language": language,
        "source": "curated",
    }


async def async_pick_coding_problem(
    *,
    difficulty: str,
    topic: str,
    programming_language: str | None,
    previous_questions: list[str] | None = None,
    db: Any = None,
) -> dict[str, Any] | None:
    """Hybrid problem selection: DB cache → static bank → None (triggers AI).

    This is the preferred entry point for the interview flow.
    """
    from app.services.problem_cache import get_cached_problem

    # Build list of previously-asked problem IDs
    previous_l = "\n".join(previous_questions or []).lower()
    previous_ids = []
    for p in PROBLEM_BANK:
        if p["title"].lower() in previous_l:
            previous_ids.append(_problem_id_from_title(p["title"]))

    # Step 1: Try DB cache
    if db is not None:
        try:
            cached = await get_cached_problem(
                difficulty=difficulty,
                topic=topic,
                programming_language=programming_language,
                previous_problem_ids=previous_ids,
                db=db,
            )
            if cached:
                return cached
        except Exception as e:
            import logging
            logging.getLogger(__name__).warning("DB cache lookup failed: %s", e)

    # Step 2: Try static bank
    curated = pick_coding_problem(
        difficulty=difficulty,
        topic=topic,
        programming_language=programming_language,
        previous_questions=previous_questions,
    )
    if curated:
        return curated

    # Step 3: Return None → caller should generate via AI
    return None
