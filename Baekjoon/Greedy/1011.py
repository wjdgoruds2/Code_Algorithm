number=int(input())
for i in range(number):
    start,end=map(int,input().split())
    distance=end-start#남은 거리
    count=0#회수
    movesum=0#현재까지의 합
    move=1 #########count별 개수
    while movesum<distance:
        count+=1
        movesum+=move
        if count%2==0: ######count회수가 1,1,2,2,3,3,4,4,... 즉 1인거1개,2인거 1개, 3인거 2개, 4인거 2개....
            move+=1#########count회수가 결국 정답이기 때문에 count회수가 짝수면 다음은 +1
    print(count)


