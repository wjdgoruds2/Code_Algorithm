city = int(input())
distance=list(map(int,input().split()))
money=list(map(int,input().split()))
start=money[0]
total=0#####총합
for i in range(1,len(money)):
    if start>money[i]: ######다음 주유소 가격이 더 작으면
        total+=start*distance[i-1] ####길이와 가격 곱
        start=money[i] #초기값을 현재로 설정
    else:######다음 주유소 가격이 더 크면
        total += start * distance[i - 1]####길이와 가격 곱,초기값은 가장 작은값 그대로 둠
print(total)

