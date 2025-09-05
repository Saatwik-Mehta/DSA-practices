from typing import List

# Learnt through back and forth discussions with CHATGPT
class Solution:
    """
    PROBLEM: https://leetcode.com/problems/meeting-rooms
    Meeting Rooms

    Time Complexity: O(n log n)
    Space Complexity: O(n), due to the creation of new array
    
    This Algorithm can further be enhanced/evolved to answer most of the questions regarding Meeting Rooms, such as:
    - What's the maximum number of concurrent meetings?
    - minimum number of rooms required (LeetCode 253)
    - Rooms Usage over time

    Learning:
    - Sweeping Algorithm: https://leetcode.com/discuss/post/2166045/line-sweep-algorithms-by-c0d3m-8ebq/
      - Line Sweep (or Sweep Line) is an algorithmic technique where we sweep an imaginary line (x or y axis) and solve various problem.
      - There would be an event (entry or event) and based on that we update the information and then return result.
      - Treat each meeting as two events: +1 at start, -1 at end. Traverse sorted events; if active_meetings count ever exceeds 1 → overlap.
    - PrefixSum 
      - While learning about the best solution for the meeting rooms problem, I understood the existence of the Prefix and learnt a few things about it.
      - It's a technique which does cumulative sum of the values in an array and store it at the respective index, to access the results faster.
      - https://www.youtube.com/watch?v=xbYr9JOC2Lk - Profound Academy
      - https://www.youtube.com/watch?v=yuws7YK0Yng - ALGOSCANIO
      
   """
    
    def create_meeting_interval_events(self, nums: List):
        """
        This method creates an array of events of intervals. An interval consists of start and end time of a meeting, while an event 
        consists of start-time of a meeting. This is further used to answer many of the problems put forward such as 
        - how many rooms will be required for the meetings
        - whether a person can attend all the meetings etc.
        """
        #  Stores the events occuring, such as starting of the meeting is an event. 
        events = []
        for interval in nums:
            #  Insert start and end time of the meeting as an event occuring.
        
            # When a meeting starts insert a +1 with the start-time to show an event have started.
            events.append((interval[0], +1))

            # When a meeting ends insert a -1 with the end-time to show an event have ended.
            events.append((interval[1], -1))
        
        # Sorting on the basis of start/end-time and if they are equal then on the basis of delta.
        # This is because a meeting started and ending at the same time,
        # will have the meeting ended first and then the starting of the new meeting.
        events.sort(key=lambda x: (x[0], x[1]))
        return events

    def canAttendMeetings(self, nums: List):
        """
        How it works?
        Each interval is like an event happening at a particular time. 
        Starting of the meeting is an event, ending of the meeting is an event. 
        So, we collect these events in an array along with a delta denoting the value (+/-1) that shows whether the event has ended/started,
        then the array is sorted based on the time and delta, that represents when a meeting is starting,
        when it is ending and if any meeting is starting at the same-time as one ended.
        After the sorting, we can easily count the number of meetings happening at the same time or whether a person will be able to attend all the meetings.
        """

        active_meetings = 0
        events = self.create_meeting_interval_events(nums)
        for _, delta in events:
            if (active_meetings:=  active_meetings + delta) > 1:
                return False
        return True
    
    def maxRoomsRequired(self, nums):
        """
        Problem: https://leetcode.com/problems/meeting-rooms-ii/description/
        Meeting Rooms II

        You are given an array of meeting time intervals consisting of start and end times.
        Find the minimum number of conference rooms required so that all meetings can take place without overlap.

        Time Complexity: O(n log n)
        Space Complexity: O(n) due to the creation of new array
        """
        events = self.create_meeting_interval_events(nums)
        active_meetings = 0
        rooms_needed = 0

        # We need to know the maximum number of active meetings at a particular time and this is what will be the room requirement as well.
        for _, delta in events: 
            if (active_meetings:= active_meetings + delta) > rooms_needed:
                rooms_needed = active_meetings
        return rooms_needed


                
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
    print(f"{i+1} testcase O/P=> Max Room required: ", Solution().maxRoomsRequired(ts))


            