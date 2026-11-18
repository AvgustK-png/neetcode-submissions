from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for s in strs:
            s_sorted=tuple (sorted(s))
            anagram[s_sorted].append(s)
        return list(anagram.values())
        
