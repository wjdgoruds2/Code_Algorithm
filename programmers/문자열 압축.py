def solution(s):
    result = ""
    length = []  # 길이
    if len(s) == 1:
        return 1
    for cut in range(1, len(s) // 2 + 1): #####문자열 길이의 반 까지 cut
        count = 1
        temp = s[:cut]
        for i in range(cut, len(s), cut):  # 처음cut한거 다음비교 증가율:cut만큼  현재:현재+cut만큼 이 다음
            if s[i:i + cut] == temp:  # 뒤의 내용과 같으면
                count += 1
            else:  # 뒤의 내용과 같지 않으면
                if count == 1:  ###########연속된 숫자가 아닐경우 ex)acc=a2c  -> a의 count=0으로 초기화
                    count = ""
                result += str(count) + temp  # 전 내용 result에 입력
                temp = s[i:i + cut]  # 비교할 내용 업뎃
                count = 1  # 다시 카운트는 1로 초기화
        if count == 1:  ###########마지막 수가 연속된 숫자가 아닐경우 ex)ab=ab  ->count=1로되어 있기에 b의 count=0으로 초기화
            count = ""
        result += str(count) + temp
        length.append(len(result))
        result = ""
    return min(length)

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("xababcdcdababcdcd"))
