class Solution(object):
    def countAndSay(self, n):
        if(n == 1):
            return "1"
       
        string = "1"
        
        for i in range(2, n + 1):
            string += '$'
            length = len(string)
            count = 1
            temp = ""
            
            for x in range(1, length):
                if (string[x] != string[x-1]):
                    temp += str(count)
                    temp += string[x-1]
                    count = 1
                else:
                    count += 1
            string = temp
        return string