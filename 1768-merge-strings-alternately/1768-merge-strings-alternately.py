class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        m = len(word1)
        n = len(word2)
        for i in range(min(m, n)):
            output.append(word1[i])
            output.append(word2[i])
        if m < n:
            output.append(word2[m:])
        elif m > n:
            output.append(word1[n:])
        return "".join(output)
        