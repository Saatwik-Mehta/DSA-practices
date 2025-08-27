from typing import List

class Solution:
    """
    Problem Link: https://leetcode.com/problems/two-sum/description/
    - Two Sum unsorted!
    
    Learnings:
    - Handle a hash for lookup of second number in the two sum.
    - Otherwise, insert and continue the flow.
    """
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # - don't return same element twice - means the number on the same index x and y
        #   pointing to the same index.
        # - exactly one solution for each target
        # - return in any order

        # Optimised solution:
        # create a hash that registers unique item and it's index as the value
        # start a pointer for the iterating

        # Now, run a while loop from 0 to len(nums)-1,
        # and check for the other number, by subtracting the number at index i from target,
        # now, if other number already exists in the hash, return the value(index of the other number)
        #  from the hash as well as the i index

        # otherwise store the number at ith index in the hash,
        # which will be checked as the other number in the next iternation

        check_other_number = {}
        i = 0

        while i < len(nums):
            y = target - nums[i]
            if y in check_other_number:
                return list((check_other_number[y], i))
            check_other_number[nums[i]] = i
            i+=1
        return "result not found"
        
    
