class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq = {}

        for s in strs:
            print = ("".join(sorted(s)))

            if print not in freq:
                freq[print] = []
            freq[print].append(s)  
        return list(freq.values())            
