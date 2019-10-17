class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        min_length = len(strs[0])
        previous = " "
        for i in strs:
            if len(i) < min_length:
                min_length = len(i)
                
        for length in range(min_length, 0, -1):
            match = True
            prefix = strs[0][:length]
            for w in strs:
                if w[:length] != prefix:
                    match = False
                    break
            if match:
                return prefix
        return ""