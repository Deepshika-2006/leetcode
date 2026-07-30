class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        act=n*(n+1)//2
        curr=sum(nums)
        return act-curr
        