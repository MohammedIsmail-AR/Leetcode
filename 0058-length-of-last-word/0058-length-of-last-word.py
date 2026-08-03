class Solution(object):
    def lengthOfLastWord(self, s):
        lenght = 0 

        for i in s.strip()[::-1]:
            if i == " ":
                return lenght
            lenght += 1
        return lenght 


          

                
       