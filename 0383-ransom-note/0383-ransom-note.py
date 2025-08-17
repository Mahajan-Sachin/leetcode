class Solution:
    def canConstruct(self, ransom: str, mag: str) -> bool:
        freq_ran=Counter(ransom)
        freq_mag=Counter(mag)
        for char,val in freq_ran.items():
            if freq_mag[char]<val:
                return False
        return True

        