#####문제1
# def solution(arr):
#     answer = []
#     answer.append(arr[0])
#     for i in range(1,len(arr)):
#         if answer[-1]!=arr[i]:
#             answer.append(arr[i])
#     return answer
# print(solution([1,1,3,3,0,1,1]))
# print(solution([4,4,4,3,3]))
#####문제2
def solution(n, lost, reserve):
    new_lost=set(lost)-set(reserve)
    new_reserve=set(reserve)-set(lost)
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)

    return n-len(new_lost)
print(solution(5,[2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))
print(solution(3,[1, 2],[1, 2, 5]))