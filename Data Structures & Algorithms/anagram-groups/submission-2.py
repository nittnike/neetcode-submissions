class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        groups = {}
        for words in strs:
            sorted_words = "".join(sorted(words))
            if sorted_words not in groups:
                groups[sorted_words] = [words]
            else:
                groups[sorted_words].append(words) 
        return list(groups.values())