import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[\W_]+', '', s).lower()
        print(string)
        i = 0
        j = len(string)-1
        while j >= i:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True