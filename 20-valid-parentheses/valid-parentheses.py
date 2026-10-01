class Solution:
    def isValid(self, s: str) -> bool:
        f={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        if f.get('(',0)!=f.get(')',0) or f.get('{',0)!=f.get('}',0) or f.get('[',0)!=f.get(']',0):
            return False
        stack=[0]*len(s)
        top=-1
        c=0
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack[top+1]=i
                top+=1
            elif i==')':
                if stack[top]=='(':
                    top-=1
                else:
                    c+=1
                    break
            elif i=='}':
                if stack[top]=='{':
                    top-=1
                else:
                    c+=1
                    break
            elif i==']':
                if stack[top]=='[':
                    top-=1
                else:
                    c+=1
                    break
        if c>0:
            return False
        else:
            return True