class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        alphanumeric=[]
        for i in s:
            if 97<=ord(i.lower())<=122:
                alphanumeric.append(i.lower())
        n=len(alphanumeric)
        for j in range(n):
            if alphanumeric[j]!=alphanumeric[n-j-1]:
                return False
        return True
        
