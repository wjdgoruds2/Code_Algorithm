from itertools import product
# def solution(numbers, target):
#     l=[(x,-x) for x in numbers]
#     r=list(map(sum,product(*l)))
#     return r.count(target)

#########dfs 풀이
# def dfs(array, numbers, target, size):
#     answer = 0
#     if len(array) == size:
#         if sum(array) == target:
#             return 1
#         else:
#             return 0
#     else:
#         A = numbers.pop(0)
#         for i in [1, -1]:
#             array.append(A * i)
#             answer += dfs(array, numbers, target, size)
#             array.pop()
#         numbers.append(A)
#         return answer
# def solution(numbers, target):
#     answer = 0
#     answer += dfs([numbers[0]], numbers[1:], target, len(numbers)) ###+일때
#     answer += dfs([-numbers[0]], numbers[1:], target, len(numbers)) ####-일때
#     return answer

#########bfs
import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):  #num_idx numbers의 위치번호
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1)) #num_idx에서 나올 수 있는 +경우
            stack.append((current_sum-number, num_idx + 1))#num_idx에서 나올 수 있는 -경우

    return answer
print(solution([1, 1, 1, 1, 1],3))

