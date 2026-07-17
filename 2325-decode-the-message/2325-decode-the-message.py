class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping={}
        alphabet= "abcdefghijklmnopqrstuvwxyz"
        idx=0
        for c in key:
            if c!=" " and c not in mapping:
                mapping[c]=alphabet[idx]
                idx+=1
        return "".join(mapping[c] if c != " " else " " for c in message)
        