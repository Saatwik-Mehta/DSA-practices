from typing import List


class Solution:
    """
    PROBLEM: https://leetcode.com/problems/contains-duplicate/
    Contains Duplicate

    Time Complexity: O(n)
    Space Complexity: O(1) or worst case if array is unsorted O(n)

    Learning:
    - Even though Python uses Tim Sort which has best case Space complexity -> O(1)
    - There are cases where it's Space Complexity is O(n)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Optimised Solution
        # Using sorting and two-pointers
        # Sort the array 
        # compare the values of the array with each other to check if the digits are similar
        # return true if similar value is found
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False