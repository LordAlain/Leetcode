class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char = 0

        for ch in s+t:
            char ^= ord(ch)
        
        return chr(char)