import re #re모듈 사용해서 정규식으로 풀었음

def solution(new_id):
    answer = ''
    #소문자
    new_id=new_id.lower()
    #알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub(r'[^a-z\-\.\_\d]','', new_id)
    #2번 이상 연속된 부분을 하나의 마침표(.)
    new_id = re.sub(r'\.\.+', '.', new_id)
    #처음이나 끝에 위치한다면 제거(^시작,\문자 알림,$끝)
    new_id = re.sub(r'^\.', '', new_id)
    new_id = re.sub(r'\.$', '', new_id)
    #빈 문자열이라면, new_id에 "a"를 대입
    if len(new_id)==0:
        new_id='a'
    #길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    new_id = re.sub(r'\.$', '', new_id[0:15])
    #new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입
    while(len(new_id))<3:
        new_id+=new_id[-1]
    answer=new_id
    return answer
