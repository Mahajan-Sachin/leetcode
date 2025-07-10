class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq1 = {}
        freq2 = {}
        result = []

        for char in p:
            freq1[char] = freq1.get(char, 0) + 1

        i = 0
        j = 0

        while j < len(s):
            freq2[s[j]] = freq2.get(s[j], 0) + 1

            if j - i + 1 < len(p):
                j += 1
            elif j - i + 1 == len(p):
                if freq1 == freq2:
                    result.append(i)
                freq2[s[i]] -= 1
                if freq2[s[i]] == 0:
                    del freq2[s[i]]
                i += 1
                j += 1

        return result
