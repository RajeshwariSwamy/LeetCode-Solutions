class Solution(object):
    def twoSum(self, nums, target):
        
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num            
            if complement in num_map:
                return [num_map[complement], i]            
            num_map[num] = i
nums = [10, 100, -5, 9, 0, 11, 23, -2]
target = 100            
sol = Solution()
print(sol.twoSum(nums, target)) 