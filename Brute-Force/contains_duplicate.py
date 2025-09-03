from typing import List


class Solution:
    """
    PROBLEM: https://leetcode.com/problems/contains-duplicate/
    Contains Duplicate

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Learning:
    My solution:
    - Simple, clear and understandable, but not the best
    - nums.count() scans everytime the whole array, even if the duplicate is found
    - This slows down the brute force
    - best case O(n^2)

    ChatGPT ****
    - Classic Nested loop
    - Compare element at ith to every other element in the array
    - Returns as soon as one atleast duplicate is found
    - comparision is cheap, no extra O(n) operation
    - best case O(1)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        # BRUTE FORCE
        # This solution is based on Brute Force

        # Using a for-loop to iterate through each number and check whether it's count is 
        # greater than 1, if it is return true
        for i in nums:
            if nums.count(i) > 1:
                return True
        return False

    def containsDuplicate_chatGPT(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
                    