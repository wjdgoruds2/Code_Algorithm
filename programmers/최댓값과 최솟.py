def solution(s):
    answer = ''
    new_s=list(map(int,s.split(' ')))

    return str(min(new_s))+' '+str(max(new_s))
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))