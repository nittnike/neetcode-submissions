class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adict = {}
        for j in nums:
            if j in adict:
                adict[j] += 1
            else:
                adict[j] = 1

        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num, freq in adict.items():
            bucket[freq].append(num)
        result = []
        for i in bucket[::-1]:
            for j in range(len(i)):
                result.append(i[j])
                if len(result)== k:
                    break
            if len(result)== k:
                    break
        return result
