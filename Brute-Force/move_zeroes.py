from typing import List


class Solution:
    """
    PROBLEM: https://leetcode.com/problems/move-zeroes/description/
    Move Zeroes

    - BRUTE FORCE
    - Time Complexity: O(n^2)
    - Space Complexity: O(1) - in place 

    Learning:
    
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        ==============
        BRUTE FORCE implementation only
        ============== 
        - Requirement is to swap the zero with non-zero element on the right side; swap when -> 0 | 2
        - No zeroes should be skipped
        - if non-zero item is at left and zero is at right do not swap

        Approach 1:
        - the branched approach is checking whether element at the left is non-zero or element at the right is zero,
        then don't swap, as this will not lead us to the solution.
        - if the condition satisfies, then, swap the items
        - code also handles when two consecutive zeroes are encountered, making sure that first zero from the left should be first swapped.
        - when a specific swap happens, then the loop is broken, this is to make sure no unnecessary iteration happens, as we cannot increment i's index.
        - swaps are also less, as they are only made when the condition for swapping satisfies
        """
        n = len(nums)

        # Approach 1
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[i] != 0:
                    break
                elif nums[j] == 0:
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        # Approach 2:
        # This is the minified version of approach 1 and also taken some insipiration from chatgpt approach
        # Instead of having so many if-else branch we combine them and loop thru the items that comes after item at i-index
        # to make sure no unnecessary comparisions are happening, we break the code as soon as the swap happens.
        # The reason to not increment the i here as well as it is in the for-loop and even if we had written it through while loop,
        # there could be cases where not all zeroes would be shifted.
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        # Approach 3
        # Chat GPT approach -> 
        # Simpler, more explainable to anyone
        # Could be the best brute force
        # But, takes more iterations as compared to the solutions above
        # the iteration starts from 0 everytime in the nested for-loop for each ith index
        # Non-mandatory iternations where both the item at index j and j+1 are non-zero in the array
        # it doesn't skip 

        # ** In best comparion the above two would have found the perfect match for swapping and swapped at the earliest.
        for i in range(n):
            for j in range(n-1):
                if nums[j] == 0 and nums[j+1] != 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]