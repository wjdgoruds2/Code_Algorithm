from itertools import combinations
########런타임 에러남
# def solution(d, budget):
#     for i in range(len(d),0,-1):
#         r=list(map(sum,combinations(d,i)))
#         if min(r)<=budget:
#             return i
def solution(d, budget):
    d.sort()
    while budget<sum(d):
        d.pop()
    return len(d)


print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))
