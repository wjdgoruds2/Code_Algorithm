def solution(s):
    s = s.split(' ')
    answer = ''
    for i in range(len(s)):
        s[i] = s[i].capitalize()  # capitalize -> 앞은 대문자 뒤는 소문자로 바꿔줌
    answer = ' '.join(s)
    return answer

print(solution("3people unFollowed me"))
print(solution("3"))
print(solution("3PEO    223nFollowed 3G"))