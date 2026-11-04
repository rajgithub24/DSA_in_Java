class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        i = 0
        j = len(s) -1
        arr = list(s)
        while i < j:
            if arr[i] not in vowel:
                i +=1
            elif arr[j] not in vowel:
                j -=1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i +=1
                j -=1
        res = "".join(arr)        
        return res                