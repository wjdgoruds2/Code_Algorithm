number=int(input())
weight=[]
for i in range(number):
    value=int(input())
    weight.append(value)
weight.sort() #######################################내림차순으로 정리해서 해도됨
max=0
for a in range(len(weight)):
    if max<= weight[a]*(len(weight)-a): #기준값 * 기준값 보다 큰 값들의 개수=최종값
        max=weight[a]*(len(weight)-a)
print(max)


