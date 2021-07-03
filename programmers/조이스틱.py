def solution(name):
    answer = 0
    ###############ord('문자')->ascii 숫자변환
    last=len(name) - 1
    for i,char in enumerate(name):
        if char =='A':
            pass
        elif ord(char)-ord('A') <= 13:
            answer+=ord(char)-ord('A')
        else:
            answer += ord('Z') - ord(char) + 1
        next=i+1
        while next < len(name) and name[next] == 'A': #########A가 반복되는 구간모두 계산
            next += 1
        last = min(last, i + i + len(name) - next)  #i:현재 위치  i:현재 위치만큼 앞으로 이동  len(name)-next:뒤에서 해당위치까지 이동
    answer+=last
    return answer
# print(solution("JEROEN"))
# print(solution("JAN"))
print(solution("ANN"))