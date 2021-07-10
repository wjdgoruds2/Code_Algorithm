def solution(s):
    answer = ''
    count=0
    for i in range(len(s)):
        if s[i].isalpha()==True:
            if count%2==0:
                answer+=s[i].upper()
                count+=1
            else:
                answer += s[i].lower() ################대문자일수도있음
                count += 1
        else:
            count=0
            answer += ' '
    return answer

print(solution("try hello world"))