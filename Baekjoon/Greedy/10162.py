total=int(input())
time=[300,60,10]
answer=[]
count=0
for i in time:
    answer.append(total//i)
    total=total%i
if total>0:
    print(-1)
else:
    for num in answer:
        print(num,end=' ')
