class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sq=[i*i for i in nums]
        # sq.sort()
        # return sq
        ans=[]
        for i in nums:
            sq=i*i
            ans.append(sq)
            ans.sort()
        return ans