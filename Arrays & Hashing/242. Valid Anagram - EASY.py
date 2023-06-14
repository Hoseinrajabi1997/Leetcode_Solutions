class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp_s = {}
        temp_t = {}
        for i in range(len(s)):
            temp_s[s[i]] = 1 + temp_s.get(s[i], 0)
            temp_t[t[i]] = 1 + temp_t.get(t[i], 0)
        return temp_s == temp_t