import re
class Test:
    def isPalindrome(self,s:str)->bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]','',s)
        return s == s[::-1]
w1=Test()
w2=Test()
print(w1.isPalindrome("A man, a plan, a canal: Panama"))
print(w2.isPalindrome("race a car"))