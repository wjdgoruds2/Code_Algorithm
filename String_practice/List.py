class Test:
    def __init__(self):
        pass
    def isPalindrome(self,s:str)->bool:
        strs=[]

        for char in s:
            if(char.isalnum()):
                strs.append(char.lower())
        while(len(strs)>1):
            if(strs.pop(0) != strs.pop()):
                return False
        return True
w1=Test()
w2=Test()
print(w1.isPalindrome("A man, a plan, a canal: Panama"))
print(w2.isPalindrome("race a car"))