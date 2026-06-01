class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in range(len(nums)):
            a.add(nums[i])
        return len(a)!=len(nums)
        