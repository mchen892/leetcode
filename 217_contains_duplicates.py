class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      """
      Given an integer array nums, return true if any value
      appears at least twice in the array, and return
      false if every element is distinct.
      """
        dupes = set()
        for i in nums: 
            if i in dupes: 
                return True 
            else: 
                dupes.add(i)
        return False