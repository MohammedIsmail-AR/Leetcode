class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        counting = False

        for c in s:
            if c != " ":
                if not counting:
                    counting = True
                    length = 1
                else:
                    length += 1
            else:
                counting = False
        
        return length
        