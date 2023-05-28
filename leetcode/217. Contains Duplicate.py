class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setA = set(nums)
        if len(nums)==len(setA):
            return False
        else:
            return True
        