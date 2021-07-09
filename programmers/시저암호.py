def solution(s, n):
    answer=''
    for i in s:
        ascii_num = 0
        if i != ' ':
            ascii_num=(ord(i)+n)
            if (i.islower()==True and ascii_num>122) or (i.islower()==False and ascii_num>90):
                ascii_num-=26
            answer+=chr(ascii_num)
        else:
            answer +=' '
    return answer
print(solution("AB",1))
print(solution("z",1))
print(solution("a B z",4))