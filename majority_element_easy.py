'''
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''

class Solution:
    def __init__(self):
        pass

    def majorityElement(self, nums):
        cuttoff = len(nums)//2
        num_count = {num:0 for num in nums}
        for num in nums:
            num_count[num] +=1
        for num, count in num_count.items():
            if count>cuttoff:
                return num

'''
Boyer-Moore Voting Algorithm
The key idea is to maintain a candidate for the majority element and a counter. We iterate through the array and adjust the counter based on whether the current element matches the candidate.

Canceling out to turn counter of majority element to zero wont be possible since it occurs more than half( of length of nums) times.
'''         
class Solution:
    def __init__(self):
        pass

    def majorityElement(self, nums):
        candidate = None
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num

            counter += 1 if candidate == num else (-1)
        
        return candidate
