#list와 dic의 조합
def solution(record):
    answer = []
    new=[] #split 제거 배열 (굳이 사용 안하면 record.split(' ')[ ])
    info={} #id와 이름
    for i in record:
        new.append(list(i.split())) #공백제거해서 list만듬
    for i in new:
        if i[0]== 'Enter' or i[0]== 'Change':
            info[i[1]]= i[2] #이름을 변경
    for j in new:
        if j[0]=='Enter':
            answer.append(info[j[1]]+"님이 들어왔습니다.")
        elif j[0]=='Leave':
            answer.append(info[j[1]]+"님이 나갔습니다.")
        elif j[0] == 'Change':
            pass
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))