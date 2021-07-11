def solution(n, m):
    if n<=m:
        if m%n==0:
            return [n,m]
        else:
            for i in range(n-1,0,-1):
                if n%i==0 and m%i==0:
                    return [i,(m*n)//i]
    else:
        if n%m==0:
            return [m,n]
        else:
            for i in range(m-1,0,-1):
                if n%i==0 and m%i==0:
                    return [i,(m*n)//i]


print(solution(7,12))
# print(solution(12,4))
# print(solution(1,5))