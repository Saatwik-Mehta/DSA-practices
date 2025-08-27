from typing import List

class Solution:
    """
    Problem Link: https://leetcode.com/problems/two-sum/description/
    - Two Sum unsorted!
    
    Learnings:
    - Using two pointers without sorting the array will not work, even if the array is sorted and reversed.
    - We have to first sort it in ascending order.
    """


    # Time Complexity: O(n log n) -> Sorting operation (TIM SORT)
    # Space Complexity: O(n) -> New array being created
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # - don't return same element twice - means the number on the same index x and y
        #   pointing to the same index.
        # - exactly one solution for each target
        # - return in any order

        # Optimised solution:
        # start i from index 0 and j from end index of the array,
        # create a list of tuple of index and number, that stores the original index of the number for the final result.
        # sort the newly created list accoding to the number key in ascending, so that two-pointer approach can be applied.
        # start a while loop with condition i < j,
        # compare the sum with the target if it's equal return
        # if the sum is smaller, increment i and retry,
        # if the sum is greater, decrement j and retry.

        i = 0
        j = len(nums) - 1
        # O(n) -> for space complexity for new array being created
        nums = [(index, number) for index, number in enumerate(nums)]

        # O(n log n) -> time complexity for sorting operation
        nums.sort(key= lambda x: x[1])
        print(nums)
        while i < j:
            if nums[i][1] + nums[j][1] == target:
                return list((nums[i][0], nums[j][0]))
            elif nums[i][1] + nums[j][1] > target:
                j -= 1
            else: i += 1
        return "result not found"