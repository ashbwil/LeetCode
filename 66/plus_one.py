class Solution(object):
    def plusOne(self, digits):
        x = len(digits)-1
        digits[x] = digits[x]+1
        while digits[x] == 10:
            digits[x] = 0
            if x == 0:
                digits.insert(0,1)
                break
            digits[x-1] = digits[x-1] + 1
            x = x - 1
            if digits[0] == 0:
                digits.insert(0, 1)
                
            
        return digits
        