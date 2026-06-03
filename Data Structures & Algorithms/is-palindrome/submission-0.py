class Solution:
    def isPalindrome(self, s: str) -> bool:
       a = ""
       for i in s:
        if i.isalnum():
            a = a + i.lower()
       b = a[::-1]
       return a == b
        