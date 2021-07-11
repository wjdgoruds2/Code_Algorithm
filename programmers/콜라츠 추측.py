def solution(num):
    count=0
    while(1):
        if num==1:
            return count
        if count>500:
            return -1
        if num%2==0:
            num=num//2
        else:
            num=num*3+1
        count+=1

print(solution(6))
print(solution(16))
print(solution(626331))
