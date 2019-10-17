class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        final = 0
        if s == "":
            return 0
        for x in s:
            if x.isalpha():
                count = count + 1
                final = count
            else:
                count = 0
        return final