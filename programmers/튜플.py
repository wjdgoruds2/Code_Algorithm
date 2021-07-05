def solution(s):
    arr=[]
    answer=[]
    s = s[2:-2].split("},{")#},{를 기준으로 나눠줌
    for i in range(len(s)):
        res=s[i].split(',')
        arr.append(set(res))
        print(arr)
    arr.sort(key=len)##아래식과 동일
    # arr.sort(key=lambda x:len(x)) #####{}길이로 정렬
    alredy=set()
    for i in arr:
        temp=i-alredy #####현재-answer해서 answer에 없는 값 추가
        answer.append(list(temp)[0])
        alredy = i
    return [int(k) for k in answer]
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))