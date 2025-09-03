from typing import List


class Solution:
    
    """
    PROBLEM 169: https://leetcode.com/problems/majority-element/
    MAJORITY ELEMENT

    TIME COMP.: O(N^2)
    SPACE COMP.: O(N) 
    """
    def majorityElement(self, nums: List[int]) -> int:
        
        # BRUTE FORCE
        # Maintain a pointer to the current number and a hash to store the count as key and
        # c_number as the value

        # Sort the array using inbuilt sort method -> O(n log n), 
        # this collects similar items together and we dont have to 
        # run count on each of the number.

        # in the for loop check if the c_number and number at Ith index are not same, 
        # set c_number as that number and store the count of the number in the hash
        # using the inbuilt count method

        # at the end check the max key and return it's value
        c_number = float('-inf')
        count_hash = {}
        nums.sort()

        for i in range(len(nums)):
            
            if nums[i] != c_number:
                c_number = nums[i]
                count_hash[nums.count(c_number)] = c_number
        return count_hash[max(count_hash)]
        

        
            

