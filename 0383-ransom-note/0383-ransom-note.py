class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
        for char in ransom:
            if ransom[char] > mag[char]:
                return False
        return True

        