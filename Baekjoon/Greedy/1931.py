num=int(input())
time=[]
for _ in range(num):
    start,end=map(int,input().strip().split(' '))
    time.append([start,end])
time.sort(key = lambda x: (x[1], x[0])) ####################끝나는 시간 오름차순, 시작 시간 오름차순
last = time[0][1]
count=1
for n in range(1,len(time)):
    if last<=time[n][0]:
        last=time[n][1]
        count+=1
print(count)
