from typing import List

class Solution:
    """
    Brute Force: 
    Problem: https://leetcode.com/problems/meeting-rooms-ii/description/
    Meeting Rooms II

    You are given an array of meeting time intervals consisting of start and end times.
    Find the minimum number of conference rooms required so that all meetings can take place without overlap.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Learnings:
    - Understanding the exact intention of the question is always mandatory to get to the final solution. 
    - State the problem in your own words think through the requirement and solution in your mind and visualize as much as possible.
    - Finally, create your own Test cases and dry-run you login on it. 
    """
    def find_active_meetings(self, nums: List):
        # This Problem is asking to solve the max number to be alloted for the meetings. 
        # So, to find the solution we need to know at a certain point how many max meetings are active.
        # We loop through each intervals and compare them with every other intervals, 
        # and if they overlap we should increment the count by 1.
        # Once the loop is ended, the active meeting count is compared with max_room needed, if the requirement is fulfilled,
        # max_rooms will be found and returned.

        # Initially no rooms will be alloted
        max_rooms = 0
        
        for i in range(len(nums)):
            
            # Default will be 1 since, there is an interval for which the comparision will be initiating.
            count_active_meets = 1
            
            for j in range(len(nums)):    
                # In the nested loop, we are checking few things such as:
                # - Whether we are not matching the same intervals, 
                # - Whether the intervals being compared are overlapping or not
                # if they satisfy, i.e., internvals are not same and overlapping is found
                # active-meetings count will be incremented by 1
                if (i!=j) and ((nums[i][0] < nums[j][1]) and (nums[j][0] < nums[i][1])):
                    count_active_meets += 1

            # for that interval, max_rooms needed will be updated only if already max_rooms needed are not enough.
            max_rooms = count_active_meets if max_rooms < count_active_meets else count_active_meets
        return max_rooms

testcases = [
    [[0,30],[5,10],[15,20]],                            # false
    [[7,10],[2,4]],                                     # true
    [[5,10],[0,6]],                                      # false
    [[1,5],[5,10],[10,15]],                             # true
    [[1,5],[4,6]],                                      # false
    [[10,20]],                                          # true
    [[1,3],[2,4],[4,6],[5,7]],                          # false
    [[0,5],[6,10],[11,15],[16,20]],                     # true
    [[i, i+1] for i in range(0, 10000, 2)],             # true
    [[i, i+2] for i in range(0, 10000, 1)],             # false
    [[100,200],[50,60],[61,120],[121,180],[181,300],
    [10,20],[20,30],[400,500]],                         # false
    [[0,10],[1,2],[3,4],[5,6],[7,8]],
    [[0,10],[5,15],[10,20]]
]


for i, ts in enumerate(testcases):                
    print(f"{i+1} testcase O/P: ", Solution().find_active_meetings(ts))
