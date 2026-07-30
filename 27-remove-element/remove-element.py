class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in nums:
            if i != val:
                ans.append(i)
        nums[:] = ans
        return len(ans)