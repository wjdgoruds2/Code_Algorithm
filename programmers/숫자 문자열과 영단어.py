def solution(s):
    num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    # if s.isdigit(): #########굳이 할필요는 없음
    #     return s
    for num,name in num.items():
        if name in s:
            s=s.replace(name, str(num))
    return s
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))