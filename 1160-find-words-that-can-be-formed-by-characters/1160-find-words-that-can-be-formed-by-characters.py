class Solution:
    def countCharacters(self, words, chars):
        chars_count = Counter(chars)
        return sum(len(word) for word in words if not Counter(word) - chars_count)