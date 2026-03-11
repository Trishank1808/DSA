class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b=bin(n)[2:]
        comp=""
        for i in b:
            if i=='0':
                comp+='1'
            else:
                comp+='0'
        return int(comp ,2)


        