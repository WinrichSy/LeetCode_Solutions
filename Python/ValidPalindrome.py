#Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~` '''

        if len(s)==0:
            return True

        for x in s:
            if x in punctuations:
                s = s.replace(x, "")

        s=s.lower()

        end = len(s)-1
        for i in range(len(s)/2):
            if s[i]!=s[end]:
                return False
            end -= 1


        return True
