def solution(a, b):
    # return sum(range(min(a,b),max(a,b)+1))
    # return sum(range(a,b+1) if a<=b else range(b,a+1))
    return sum([num for num in range(a, b + 1)]) if a <= b else sum([num for num in range(b, a + 1)])


print(solution(3,5))