num = int(input())
count=0
while(1):
    if num%5==0:
        print(count+(num//5))##########3으로 나눠떨어지든 5로 나눠떨어지든 결국 num=0이면 여기서 출력
        break
    num-=3
    count+=1
    if num<0:
        print(-1)
