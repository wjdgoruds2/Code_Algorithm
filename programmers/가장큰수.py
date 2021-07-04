from itertools import permutations
def solution(numbers):
########################################################시간 초과##########################################
    # arr=list(permutations(numbers,len(numbers)))
    # num_arr=[''.join(map(str,num)) for num in arr]
    # return max(num_arr)
    arr=list(map(str,numbers))
    arr.sort(key=lambda x:x*3,reverse=True)
    return str(int(''.join(arr)))
# lambda x : x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다.
# x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.(각 수의 첫번째만 비교하면됨)
# 이 문제의 핵심이라고 할 수 있다.


print(solution([6, 10, 2]))
print(solution([0,0]))
print(solution([3, 30, 34, 5, 9]))