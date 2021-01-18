class Test:
    def longPalindrome(self,s:str)->str:
        def expand(left:int,right:int)->str:
            while left >= 0 and right < len(s) and s[left] == s[right]: #같은 거 두단어를 기준으로 앞뒤가 같은지 비교
                left -= 1
                right += 1
            return s[left + 1:right] #안같으면 return
        if len(s) < 2 or s == s[::-1]:
            return s
        result=''
        for i in range(len(s)-1):
            result = max(result,expand(i, i+1),expand(i, i+2),key=len) #단어수를 짝수개 홀수개 나눠서 계산
        return result
w1=Test()
print(w1.longPalindrome("babad"))