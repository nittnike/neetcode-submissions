class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j)-ord("a")] += 1
            temptup = tuple(count)
            if temptup not in adict:
                adict[temptup] = [i]
            else:
                adict[temptup].append(i)
        
        return list(adict.values())
        