'''
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''


'''
Approach 1 : Recursion
Time Complexity: 0(n*2^n)
'''
class Solution:
    def __init__(self):
        pass

    def combinationSum(self, candidates, target):
        candidates.sort()
        index = 0
        possible_combinations = []
        while (index < len(candidates)):
            current_candidate = candidates[index]

            if current_candidate > target:
                break

            if current_candidate == target:
                possible_combinations.append([current_candidate])
                break
            
            multiplier = 1
            candidate_product = current_candidate
            while candidate_product <= target:
                candidate_array = [current_candidate for i in range(multiplier)]
                if candidate_product == target:
                    possible_combinations.append(candidate_array)
                    break

                other_elements = self.combinationSum(candidates[index+1:], target - candidate_product)
                for element in other_elements:
                    possible_combinations.append(element + candidate_array)
                multiplier+=1
                candidate_product = current_candidate * multiplier
            
            index+=1

        return possible_combinations

candidates = [2,3,5]
target = 8
solution = Solution()
possible_combinations = solution.combinationSum(candidates, target)
print(possible_combinations)