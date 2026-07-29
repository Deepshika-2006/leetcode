class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v=[]
        n=[]
        for i in nums:
            if i==val:
                v.append(i)
            else:
                n.append(i)
                
        # Copy the correct elements back into the original nums array
        nums[:len(n)] = n
        
        return len(n)
