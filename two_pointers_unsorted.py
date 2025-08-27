from typing import List

class Solution:

    # Time Complexity: O(n log n) -> Sorting operation (TIM SORT)
    # Space Complexity: O(n) -> New array being created
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
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
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
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
        
    
