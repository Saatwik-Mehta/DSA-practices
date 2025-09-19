from typing import List

class Solution:
    """
    Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/
    - 977. Squares of a Sorted Array
    
    Learnings:
    - Bubble sort is worse even if we compare to other O(n^2) algo doing the sorting
    - Even if the array is sorted it will still loop through each item, making time complexity O(n^2)
    - This solution can further be enhanced without using any inbuilt sorting algo to practice any other sorting algo. 
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Brute Force: Not the best solution in the market! also, fails when the input is too big!

        Here is the simplest solution one can think of to this problem
        - You have the array sorted already
        - You square each item in the array, and place at the same index inside the new array as the original number that was squared
        - Now, the new array is unsorted, and we need to sort that array
        - I used the simplest bubble sort here, to keep the solution easy and understandable. 

        - Here are my findings, on bubble sort. 
        - It's the worst solution even if we compare other O(n^2) solution in the market (insertion, selection etc.)
        - This Algo have the time complexity of O(n^2), even if the array is sorted
        - To optimize the solution, I had to keep a check and break when there were no swappings found, this is called enhanced bubble sorting. 
        """
        n = len(nums)
        sorted_square_arr = []
        for each_item in nums:
            sorted_square_arr.append((each_item)**2)

        for _ in range(n):
            swap_occur = False
            for j in range(n-1):
                if (sorted_square_arr[j]) > (sorted_square_arr[j+1]):
                    sorted_square_arr[j], sorted_square_arr[j+1] = sorted_square_arr[j+1], sorted_square_arr[j]
                    swap_occur = True
            if not swap_occur:
                # that means array is sorted which is basically bubble sort doesn't know
                break
        return sorted_square_arr



