def solution(s):
    return ''.join(sorted(s, reverse=True))#######AEZabcd->dcbaZEA  걍뒤집기만 하면됨
    # answer = ''
    # new_s=[i for i in s]
    # is_upper=[]
    # is_lower=[]
    # for i in new_s:
    #     if i.islower()==False:
    #         is_upper.append(i)
    #     else:
    #         is_lower.append(i)
    # print(is_lower,is_upper)
    # return ''.join(sorted(is_lower,reverse=True)+sorted(is_upper, reverse=True))

print(solution("Zbcdefg"))
print(solution("EZAbacd"))
print(solution("ZEFG"))