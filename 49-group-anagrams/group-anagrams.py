class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp in d:
                d[temp].append(i)
            else:
                d[temp] = [i]
        ans = []
        for i in d:
            row = []
            for j in d[i]:
                row.append(j)
            ans.append(row)
        return ans