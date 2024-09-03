class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for char in s:
            num += str(ord(char) - ord('a') + 1) 
        
        for _ in range(k):
            sum = 0
            for digit in num: 
                sum += int(digit) 
            num = str(sum)  
        
        return int(num)