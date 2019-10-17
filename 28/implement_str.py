class Solution(object):
    def strStr(self, haystack, needle):
        length_needle = len(needle)
        n = 0
        h = 0
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        else:
            while n < length_needle:
                if haystack[h] == needle[n]:
                    h = h + 1
                    n = n + 1
                    final = h - length_needle
                else:
                    h = h - n + 1
                    n = 0
            return final