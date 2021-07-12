########gcd함수 사용해도됨(최대공약수)
def solution(arr):
    arr.sort()
    minni=0
    for i in range(1,len(arr)):
        if minni==0:
            minni=minimum(arr[i-1],arr[i])
        else:
            minni=minimum(minni, arr[i])
    return minni
def minimum(num1,num2):
    a,b=min(num1,num2),max(num1,num2)
    mul=a*b
    if b%a==0:
        return b
    while b>0:
        a,b=b,a%b
    return mul//a

print(solution([2,8,6,14]))
print(solution([1,2,3]))