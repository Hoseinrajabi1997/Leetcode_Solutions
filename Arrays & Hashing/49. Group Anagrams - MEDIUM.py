from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst  = defaultdict(list)
        for i in strs:
            letters = [0] * 26
            for j in i:
                letters[ord(j)-ord("a")] += 1
            lst[tuple(letters)].append(i)
        return lst.values()
