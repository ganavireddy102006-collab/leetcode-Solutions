class Solution(object):
    def addToArrayForm(self, num, k):
        d=int("".join(map(str,num)))
        t=d+k
        f=list(map(int,str(t)))
        return f