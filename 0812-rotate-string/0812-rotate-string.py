class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        string=s*2
        if goal in string:
            return True
        return False
        