'''
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

'''
Complexity: 0(n^2)
'''
class Solution:
    def threeSum(self, nums):
        nums.sort() # sorting enables us to use two pointer approach and to skip duplicate elements

        complementary_sum_for_zero = []
        for num in nums:
            complementary_sum_for_zero.append(0-num)
        
        eligible_nums = []
        for index, target in enumerate(complementary_sum_for_zero):
            # skip duplicate elements
            if index > 0 and (nums[index] == nums[index-1]):
                continue

            eligible_pairs = self.find_element_index_with_target_sum(nums, target, index)

            for (first_index, second_index) in eligible_pairs:
                eligible_nums.append([nums[index], nums[first_index], nums[second_index]])

        return eligible_nums

    # 2sum with two pointer aproach
    def find_element_index_with_target_sum(self, nums, target, fixed_index):
        start_pointer = fixed_index+1
        end_pointer = len(nums) -1

        eligible_list = []
        while end_pointer>start_pointer:
            current_sum = nums[end_pointer] + nums[start_pointer]
            if current_sum > target:
                end_pointer-=1
            if current_sum<target:
                start_pointer+=1
            if current_sum == target:
                if (start_pointer !=fixed_index) and (end_pointer != fixed_index):
                    eligible_list.append([start_pointer, end_pointer])

                    # skip duplicate elements
                    while end_pointer> start_pointer and nums[end_pointer] == nums[end_pointer-1]:
                        end_pointer-=1
                    while end_pointer>start_pointer and nums[start_pointer] == nums[start_pointer+1]:
                        start_pointer+=1

                start_pointer+=1
                end_pointer-=1
        
        return eligible_list

solution = Solution()
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
eligible_nums = solution.threeSum(nums)
print(eligible_nums)