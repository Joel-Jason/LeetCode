class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=0
        m=sum(nums)
        ans=[]
        for i in range(n):
            m-=nums[i]
            ans.append(abs((i*nums[i])-l)+abs(((n-1-i)*nums[i])-m))
            l+=nums[i]
        return ans