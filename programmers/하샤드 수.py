def solution(x):

        return x%sum(list(map(int,str(x))))==0
print(solution(10))
print(solution(12))
print(solution(11))