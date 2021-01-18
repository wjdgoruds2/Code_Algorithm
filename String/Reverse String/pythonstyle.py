from typing import List

class Test:
    def reverseString(self,s:List[str])->None:
        # s.reverse() #reverse는 list에만 사용이 가능
        s=s[::-1] #슬라이싱은 리스트와 문자열 모두 사용 가능
        print(s)
w1=Test()
w1.reverseString(["h","e","l","l","o"])