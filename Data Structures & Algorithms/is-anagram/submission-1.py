class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        b = dict()
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            else:
                a[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in b:
                b[t[j]] = 1
            else:
                b[t[j]] += 1
        return a==b