class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits="123456789"
        start = len(str(low))
        end = len(str(high))
        ans=[]
        for L in range(start,end+1):
            for i in range(len(digits)-L+1):
                num=int(digits[i: i+L])
                if low <= num <= high:
                    ans.append(num)
        return ans

        