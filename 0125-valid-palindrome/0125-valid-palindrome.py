class Solution(object):
    def isPalindrome(self, s):
        processed_s = "".join([x.lower() for x in s if x.isalpha() or x.isdigit()])
        return processed_s == processed_s[::-1]
        



