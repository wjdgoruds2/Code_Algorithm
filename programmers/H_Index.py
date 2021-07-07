def solution(citations):
    # answer = 0
    # citations.sort()
    # print(citations)
    # for i in range(citations[-1]+1): #최대값까지 반복
    #     l=sum(j>=i for j in citations)
    #     m=sum(j<i for j in citations)
    #     if l>=i and m<=i:
    #         if i>answer:
    #             answer=i
    # if citations[0]>len(citations):
    #     answer=len(citations)





    citations.sort(reverse=True)
    print(list( enumerate(citations, start=1))) 
    print(list(map(min,enumerate(citations, start=1))))#########################역순리스트에서 min을 통해 자신보다 큰게 몇개있는지
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
print(solution([3, 0, 6, 1, 5]))
print(solution([7, 5, 1, 1, 2,5]))
print(solution([20,21]))