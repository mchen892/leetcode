class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        x = nums[0] 
        for i in range(1, len(nums)): 
            if nums[i] == x: 
                return x 
            else: 
                x = nums[i]