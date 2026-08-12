class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adict = {}
        for j in nums:
            if j in adict:
                adict[j] += 1
            else:
                adict[j] = 1
        nlist = sorted(adict.items(), key = lambda x: x[1])
        tlist = []
        for i in range(1,k+1):
            tlist.append(nlist[-i][0])
        return tlist
      
        