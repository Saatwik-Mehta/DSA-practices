from typing import List

class Solution:
    """
    PROBLEM: https://leetcode.com/problems/meeting-rooms
    Meeting Rooms

    Time Complexity: O(n log n)
    Space Complexity: O(1) or worst case if array is unsorted O(n)

    Learning:
    - Even though Python uses Tim Sort which has best case Space complexity -> O(1)
    - There are cases where it's Space Complexity is O(n)
    - Even though at starting the problem was hard to solve, 
    - it's the searching and analysis was something that helped to understand flow
    """
    def canAttendMeetings(self, nums: List):
        # Approach: SORTING and SCANNING

        # Sort the array with the start_time(0th-index) in the nums
        nums.sort(key=lambda x: x[0])
        
        for i in range(len(nums)-1):
            # Compare the end time of the first meeting with the start time of following meeting,
            #  it will tell us whether the person can attende the meeting or not. 
            if nums[i][1] > nums[i+1][0]:
                return False
        return True
        
if __name__ == "__main__":
    print(Solution().canAttendMeetings([[1,5],[5,8]]))
    print(Solution().canAttendMeetings([[7,10],[2,4],[7, 4]]))
    print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]))

            