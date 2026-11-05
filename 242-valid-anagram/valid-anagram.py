class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_S = sorted(s)
        sort_T = sorted(t)
        if sort_S == sort_T:
            return True
        else:
            return False    
        