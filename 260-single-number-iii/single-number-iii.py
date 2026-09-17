class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        f={}
        res=[]
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for i in f:
            if f[i]==1:
                res.append(i)
        return res