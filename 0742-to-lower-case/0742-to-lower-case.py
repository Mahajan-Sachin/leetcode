class Solution:
    def toLowerCase(self, s: str) -> str:
        s=list(s)
        string=""
        for char in s:
            string+=char.lower()
        return string
        