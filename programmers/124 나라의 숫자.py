
def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        r,s=divmod(n-1,3) #이전의 수와 divmod해야함
        return solution(r)+'124'[s]
print(solution(1))
print(solution(10))
