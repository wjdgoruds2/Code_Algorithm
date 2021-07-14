import sys
total=int(input())
for i in range(total):
    people=int(input())
    count=1
    rank=[]
    for j in range(people):
        a,b=sys.stdin.readline().split() #######input()->sys.stdin.readline() 시간 초과 해결 위해
        rank.append([int(a),int(b)])
    rank=sorted(rank,key=lambda x:(x[0],x[1])) ###############오름차순으로 정렬하면 첫번째 사람은 무조건 통과고 뒷사람과 비교후 max를 현재값으로 설정
    max=rank[0][1]
    for a in range(1,len(rank)):
        if rank[a][1]<max: #############앞 사람보다 순위가 낮다면 통과
            count+=1
            max = rank[a][1]
    print(count)

