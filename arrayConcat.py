class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(x.count(" ") for x in sentences)+1