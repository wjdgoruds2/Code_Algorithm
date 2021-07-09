def solution(s):
    if s.isdigit()==True and (len(s)==4 or len(s)==6):#if s.isdigit()==True and len(s) in (4,6)
        return True
    else:
        return False
print(solution("a234"))
print(solution("1234"))