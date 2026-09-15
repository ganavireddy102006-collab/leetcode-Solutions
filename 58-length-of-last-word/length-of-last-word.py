class Solution(object):
    def lengthOfLastWord(self, s):
        f=s.split()
        return len(f[-1])