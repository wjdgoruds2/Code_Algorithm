def solution(N, stages):
    per=dict()
    len=0
    count=0
    for i in range(1,N+1):
        for j in stages:
            if j >= i:
                len+=1
                if j==i:
                    count+=1
        if len !=0:
            per[i]=count/len
        else: ####################################아무것도 해당이 안될떄 즉 len=0일때(N번까지 간 경우가 없을 떄 예외처리) //안하면 런타임에러
            per[i]=0
        len=0
        count=0
    answer = sorted(per.items(),key=lambda x:x[1], reverse=True)
    return list(x[0] for x in answer)
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
print(solution(1,[1,1,1,1,1]))