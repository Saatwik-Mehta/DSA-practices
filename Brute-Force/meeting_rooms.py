from typing import List

class Solution:
    """
    PROBLEM: https://leetcode.com/problems/meeting-rooms
    Meeting Rooms

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Learning:
    - In an unsorted manner of comparision, if the start time of interval1 is smaller than the end time of interval2,
      and the start time of interval2 is smaller than the end time of interval1, the meetings will overlap.
    - This is because the meeting 1 end time is still not reached but the meeting 2 has started which is incorrect.
    """
    def canAttendMeetings(self, nums: List):
        # Brute Force Solution
        # Using Original Nested loop concept two compare the intervals
        # If start time of interval 1 is smaller than end time of interval 2
        #  and If start time of interval 2 is smaller than end time of interval 1, there will be a conflict in the meet. 
        # Since, the second meeting starts before the first meetings ends.
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i][0] < nums[j][1] and nums[j][0] < nums[i][1]:
                    return False
        return True
        

                
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
     [10,20],[20,30],[400,500]]                         # false
]

              
for i, ts in enumerate(testcases):                
    print(f"{i+1} testcase O/P: ", Solution().canAttendMeetings(ts))

            