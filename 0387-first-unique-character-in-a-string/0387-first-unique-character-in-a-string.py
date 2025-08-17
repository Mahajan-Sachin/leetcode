class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        var=""
        for char in freq:
            if freq[char]==1:
                var=char
                break
        if var=="":
            return -1
        return s.find(var)

        