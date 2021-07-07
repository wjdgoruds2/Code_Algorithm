def solution(clothes):
    answer = 1
    clodict={}
    for i in clothes:
        if i[1] in clodict:
            clodict[i[1]]+=1
        else:
            clodict[i[1]]=1
    print(clodict)
    for i in clodict.values():
        answer*=(i+1) ######각 타입을 선택할수도 안할수도 있으니 아무것도 안입을 상태로 치고 +1

    return answer-1 #####모든 타입을 안입은 경우는 없기 때문에 최종 -1
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))