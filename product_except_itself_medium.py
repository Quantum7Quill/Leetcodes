'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

'''
Approach 1: prefix and suffix array
1,2,3,4
(1,2*3*4), (1, 3*4), (1*2,4), (1*2*3,1)

Time complexity: 0(n)
space complexity: 0(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)

        index = 1
        prefix_product = [1 for i in range(count)]
        while index<(count):
            prefix_product[index] = prefix_product[index - 1] * nums[index - 1]
            index+=1
        
        index = count-2
        suffix_product = [1 for i in range(count)]
        while index>=0:
            suffix_product[index] = suffix_product[index + 1] * nums[index + 1]
            index-=1

        final_nums = []
        index = 0
        while(index<count):
            final_nums.append( prefix_product[index] * suffix_product[index] )
            index+=1
        
        return final_nums
    

'''
Approach 2: Reduce Time complexity by using only one final array.
1        2      3       4
1,       1,    1*2,    1*2*3
2*3*4, 3*4,  4,      1 

Time Complexity: 0(n)
Space Complexity: 0(1)  If we don't consider final_nums into complexity
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)

        index = 1
        final_nums = [1 for i in range(count)]
        while index<(count):
            final_nums[index] = final_nums[index - 1] * nums[index - 1]
            index+=1
        
        index = count-2
        product = 1
        while index>=0:
            product *= nums[index+1]
            final_nums[index] = final_nums[index] * product
            index-=1
        
        return final_nums

            

            