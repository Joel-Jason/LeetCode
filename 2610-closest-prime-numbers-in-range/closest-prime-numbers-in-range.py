arr=[True]*(10**6 +1)
arr[0]=False
arr[1]=False
for i in range(2,10**3 +1):
    if arr[i]:
        j=i*i
        while j<10**6 +1:
            arr[j]=False
            j+=i
def prime(l,r):
    p=[]
    a=-1
    b=-1
    for i in range(l,r+1):
        if arr[i]:
            p.append(i)
        m=9999999
    for i in range(len(p)-1):
        if p[i+1]-p[i]<m:
            m=p[i+1]-p[i]
            a=p[i]
            b=p[i+1]
    return a,b
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        a,b=prime(left,right)
        return a,b