class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital=0
        for ch in word:
            if ch.isupper():
                capital += 1
        if capital == len(word) or capital == 0:
            return True
        if capital == 1 and word[0].isupper():
            return True
        else:
            return False

        