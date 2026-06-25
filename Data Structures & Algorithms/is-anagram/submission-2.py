class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            if i not in sdict:
                sdict[i] = 1
            else:
                sdict[i] += 1
        for j in t:
            if j not in tdict:
                tdict[j] = 1
            else:
                tdict[j] += 1
        return sdict == tdict