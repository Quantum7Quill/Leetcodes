'''
57. Insert Interval
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
'''


'''
Approach 1: 0(n)
Linear search to find insertion index: 0(n)
Linear Scan to merge intervals: 0(n)

Approach 2: 0(n)
Binary Search to find insertion index: 0(logn)
Linear Scan to merge intervals: 0(n)

'''
class Solution:
    def __init__(self, intervals, new_interval):
        final_intervals = self.insert(intervals, new_interval)
        print(final_intervals)

    def insert(self, intervals, new_interval):
        start_of_new_interval, _ = new_interval
        index = 0
        index_of_insertion = None

        # linear search to find index to insert new interval
        while index<len(intervals):
            # insert it at the first index where start of interval in list is greater than or equal to that of new_interval
            if intervals[index][0] >= start_of_new_interval:
                index_of_insertion = index
                break
            index+=1
        # Append the new interval in intervals if all interval start in the list are smaller than that of new interval
        if index_of_insertion is None:
            index_of_insertion = len(intervals)
        
        merged_list = self.merge_intervals(intervals[:index_of_insertion] + [new_interval] + intervals[index_of_insertion:])
        return merged_list
        
    def merge_intervals(self, interval_list): 
        '''
        Algo: Insert first interval in merged list.
                Iterate over rest of interval_list
                    If overlapping:
                        merge with last element of merged_list
                    else:
                        append the interval in merged_list
        '''

        if len(interval_list) == 0:
            return interval_list
        
        merged_list = [interval_list[0]]
        interval_index = 1
        while (interval_index<len(interval_list)):
            if self.is_overlapping(merged_list[-1], interval_list[interval_index]):
                merged_list[-1][1] = max(merged_list[-1][1], interval_list[interval_index][1])
            else:
                merged_list.append(interval_list[interval_index])
            interval_index+=1

        return merged_list

    def is_overlapping(self, first_interval, second_interval):
        # if start of second interval lies between start and end of first one
        if second_interval[0] >= first_interval[0] and second_interval[0]<=first_interval[1]:
            return True
        return False

intervals = [[1,5]]
new_interval = [1,7]

Solution(intervals, new_interval)