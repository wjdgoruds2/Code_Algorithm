def solution(n):
    # return sum(i for i in range(1,n+1) if n%i==0)
    return n + sum(i for i in range(1, (n // 2) + 1) if n % i == 0) ######n//2까지만 하면됨 속도 향상
print(solution(12))
print(solution(5))