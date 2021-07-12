########################중간에 공백이 여러개인 경우의 수를 생각해야함->그래서 딴걸로 하면 실패뜸
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