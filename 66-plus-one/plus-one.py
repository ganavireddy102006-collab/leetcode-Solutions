class Solution(object):
    def plusOne(self, digits):
        d=int("".join(map(str,digits)))
        t=d+1
        l=list(map(int,str(t)))
        return l        