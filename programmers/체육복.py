##########그리디##########
def solution(n, lost, reserve):
    answer = 0
    set_reserve=set(reserve)-set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost: #1 작은애
            answer+=1
            set_lost.remove(i-1)
        elif i+1 in set_lost:#1 큰애
            answer+=1
            set_lost.remove(i+1)
    return n-len(set_lost)
print(solution(	5, [2, 3, 4], [1, 3, 5]))