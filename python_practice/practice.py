# ###################변수
# name="연탄이"
# animal="고양이"
# age=4
# hobby="산책"
# is_adult=age>=3

# '''여러 문장 주석(ctrl+/)
# print("우리집 "+animal+"의 이름은 "+name+"에요")
# hobby="공놀이"
# #print(name+"는 "+str(age)+ "살이며, " +hobby+"을 아주 좋아해요")
# print(name,"는 ",age,"살이며, " ,hobby,"을 아주 좋아해요") #빈칸이 들어감
# print(name+"는 어른일까요? "+str(is_adult))'''

# station1="사당"
# station2="신도림"
# station3="인천공항"
# print(station3+"행 열차가 들어오고 있습니다.")

################연산자
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3)#2^3=8
# print(5%3)#나머지 구하기
# print(10%3)
# print(5//3)#1
# print(10//3)#3
# print(10>3)#True
# print(4>=7)#False
# print(10 < 3)#False
# print(5<=5)#True

# print(3==3)#True
# print(4==2)#False
# print(3+4==7)#True


# print(1!=3)#True
# print(not (1!=3))#False

# print((3 > 0) and (3 < 5)) #True
# print((3 > 0) & (3 < 5))#True

# print((3 > 0) or (3 > 5)) #True
# print((3 > 0) | (3 < 5))#True
# print(5 > 4 > 7)#False

######################수식

# print(2 + 3 * 4)#14
# print((2 + 3) * 4)#20
# number= 2 + 3 *4 #14
# print(number)#14
# number=number+2#16
# print(number)#16
# number +=2#18
# print(number)#18
# number*=2#36
# print(number)#36
# number/=2#18
# print(number)#18
# number-=2#16
# print(number)#16
# number%=5#1
# print (number)#1


########숫자 처리 함수
# print(abs(-5))#5
# print(pow(4,2))#16
# print(max(5,12))#12
# print(min(5,12))#5
# print(round(3.14))#3
# print(round(4.99))#5

# from math import *
# print(floor(4.99))#4
# print(ceil(3.14))#4
# print(sqrt(16))#4


######random

# from random import *
# print(random()) #0.0~1.0미만의 임의의 값 생성
# print(random()*10) #0.0~10.0미만의 임의의 값 생성
# print(int(random()*10)) #0~10미만의 임의의 값 생성
# print(int(random()*10)+1) #1~10이하의 임의의 값 생성

# print(int(random()*45)+1) #1~45이하의 임의의 값 생성

# print(randrange(1,46))#1~46미만의 임의의 값 생성
# print(randint(1,45))#1~45이하의 임의의 값 생성


#########################스터디 예제 온라인 3회 오프라인 1회
# from random import *
# offday=randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월",offday,"일로 선정되셨습니다.")

###############문자열
# sentence='나는 소년입니다.'
# print(sentence)
# sentence2="파이썬은 쉬워요."
# print(sentence2)
# sentence3="""
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)


###############슬라이싱(필요한 정보만 가져오기)
# jumin="990120-1234567"

# print("성별: "+jumin[7])
# print("연: "+jumin[0:2]) #(0~1)
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일: "+jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리: "+jumin[7:]) #7부터 끝까지
# print("뒤 7자리 (뒤에서 부터): "+jumin[-7:])#맨 뒤는 -1

###########문자열

# python="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","java"))

# index=python.index("n")
# print(index)
# index=python.index("n",index+1)#두번째 n위치
# print(index)
# print(python.find("Java")) #오류시 -1
# # print(python.index("Java")) #오류발생후 종료
# print("hi")

# print(python.count("n"))


################문자열 포맷
# print("a"+"b")
# print("a","b")

# #방법1
# print("나는 %d살 입니다." % 20)
# print("나는 %s을 좋아해요." % '파이썬')
# print("Apple은 %c로 시작해요." %"A")
# print("나는 %s살 입니다." % 20)
# print("나느 %s색과 %s색을 좋아해요." %("파란","빨강"))


# #방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아합니다.".format("파란","빨강"))
# print("나는 {0}색과 {1}색을 좋아합니다.".format("파란","빨강"))
# print("나는 {1}색과 {0}색을 좋아합니다.".format("파란","빨강"))

# #방법3
# print("나는 {age}살이며,{color}색을 좋아해요.".format(age=20,color="빨강"))

# #방법4
# age=20
# color="빨간"
# print(f"나는 {age}살이며,{color}색을 좋아해요.")

###########탈출문자
# print("백문이 불여일견 \n백견이 불여일타")
# #저도 "나도코딩"입니다.\"  \' :문장 내에서 따옴표
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

#\\:문장 내에서 \
# print("C:\\Users\\lg\\Desktop\\python_workspace>")

# #\r:커서를 맨앞으로
# print("Red Apple\rPine")

# #\b:백스페이스(한 글자 삭제)
# print("Redd\bApple")

# #\t:탭
# print("Red\tApple")

####사이트 별로 비밀번호 만들기

# site="http://youtube.net"
# re_site=site.replace("http://","")
# re_site=re_site[:re_site.index(".")]
# password=re_site[:3]+str(len(re_site))+str(re_site.count("e"))+"!"

# print("{}의 비밀번호는 {}입니다.".format(site,password))

######리스트[]

#지하철 칸별로 10,20,30명
# subway1=10
# subway2=20
# subway3=30

# subway=[10,20,30]
# print(subway)

# subway=["유재석","조세호","박명수"]
# print(subway)
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에 다음 칸에 탐
# subway.append("하하")
# print(subway)

# #정형돈씨를 유재석과 조세호 사이에 
# subway.insert(1,"정형돈")
# print(subway)

# #지하철에 있는 사람 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇명 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list=[5,2,4,3,1]
# num_list.sort()
# print(num_list)


# #순서 뒤집기
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 함께 사용
# num_list=[5,4,3,2,1]
# mix_list=["조세호",20,True]
# print(mix_list)


# #리스트 학장
# num_list.extend(mix_list)
# print(num_list)





#########사전
# cabinet={3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])


# print(cabinet.get(3))
# # print(cabinet[5]) #오류발생후 종료
# print(cabinet.get(5,"사용가능"))
# print("hi")

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# cabinet={"A-3":"유재석","B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새손님
# print(cabinet)
# cabinet["A-3"]="김종국"
# cabinet["C-29"]="조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

###########튜플(값을 추가와 같은 변경 불가능)

# menu=("돈가스","치즈가스")
# print(menu[0])
# print(menu[1])

# # name="김종국"
# # age=20
# # hobby="코딩"
# # print(name,age,hobby)
# (name,age,hobby)=("김종국",20,"코딩")
# print(name,age,hobby)


########집합(set)
#중복 안됨,순서 없음

# my_set={1,2,3,3,3}
# print(my_set)

# java={"유재석","김태호","양세형"}
# python=set(["유재석","박명수"])


# #교집합(java와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))


# #합집합
# print(java | python)
# print(java.union(python))

# #차집합(java는 할수 있지만 python은 할 줄 모르는 사람)
# print(java-python)
# print(java.difference(python))

# #python할 수 있는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java를 까먹음
# java.remove("김태호")
# print(java)

#자료구조 변경
#커피숍
# menu={"커피","우유","주스"}
# print(menu,type(menu))

# menu=list(menu)
# print(menu,type(menu))

# menu=tuple(menu)
# print(menu,type(menu))

# menu=set(menu)
# print(menu,type(menu))

###################코딩대회 추첨 예제
# from random import *
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst=range(1,21)#1~20까지 숫자 생성
# lst=list(lst)
# shuffle(lst)
####중복 발생(사용x)
# print("--당첨자 발표--")
# print("치킨 당첨자:",sample(lst,1))
# print("커피 당첨자:",sample(lst,3))
# print("--축하합니다--")

# winners=sample(lst,4)
# print("--당첨자 발표--")
# print("치킨 당첨자:{}".format(winners[0]))
# print("커피 당첨자:{}".format(winners[1:]))
# print("--축하합니다--")



################if
# weather=input("오늘 날씨는 어때요? ")
# if weather=="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather=="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp=int(input("기온은 어때요?"))
# if temp>=30:
#     print("너무 더워요.나가지 마세요")
# elif 10<=temp and temp<30:
#     print("괜찮은 날씨에요")
# elif 0<=temp<10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요.나가지 마세요")

################for
# for waiting_no in range(1,6):#1,2,3,4,5
#     print("대기번호:{0}".format(waiting_no))

# starbucks=["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0},커피가 준비되었습니다.".format(customer))

#################while
# customer="토르"
# index=5
# while index>=1:
#     print("{0},커피가 준비 되었습니다. {1}번 남았어요".format(customer,index))
#     index-=1
#     if index==0:
#         print("커피가 폐기처분되었습니다.")

# customer="아이언맨"
# index=1
# while True:
#     print("{0},커피가 준비 되었습니다. 호출 {1}회".format(customer,index))

# customer="토르"
# person="Unknown"

# while person!=customer:
#    print("{0},커피가 준비 되었습니다.".format(customer))
#    person=input("이름이 어떻게 되세요? ")


##########continue and break
# absent=[2,5]#결석
# no_book=[7]#책을 깜빡함
# for student in range(1,11):#1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#       print("{0}야 교무실로 와".format(student))
#       break
#     print("{0}야 책을 읽어봐".format(student))


######################한 줄 for
#출석번호가 1,2,3,4,5 앞에 100을 붙이기로 함->101,102...
# students=[1,2,3,4,5]
# print(students)
# students=[i+100 for i in students]
# print(students)

#학생 이름을 길이로 변환
# students=["Iron man","Thor","I am groot"]
# students=[len(i) for i in students]
# print(students)

# students=["Iron man","Thor","I am groot"]
# students=[i.upper() for i in students]
# print(students)

#####################탑승 승객 수 구하는 프로그램 예제
# from random import *
# count=0
# for people in range(1,51):#(승객)
#     time=randrange(5,50)
#     if 5<=time<=15:#매칭 성공
#         print("[o]{0}번째 손님(소요시간 : {1}분)".format(people,time))
#         count+=1
#     else: #매칭 실패
#         print("[ ]{0}번째 손님(소요시간 : {1}분)".format(people,time))

# print("총 탑승승객:{}".format(count))


#####################함수
# def open_count():
#     print("새로운 계좌가 생성되었습니다.")
# def deposit(balance,money):
#     print("입금이 완료되었습니다.잔액은 {}입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance,money):
#     if balance>=money:
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance-money))
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(balance))

# def withdraw_night(balance,money):#저녁에 출금
#     commission=100
#     return commission,balance-money-commission
# balance=0
# balance=deposit(balance,1000)
# # balance=withdraw(balance,500)
# commission,balance=withdraw_night(balance,500)
# print("수수료는 {0}원이며,잔액은 {1}입니다.".format(commission,balance))

#######################기본값
# def profile(name,age,main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
#     .format(name,age,main_lang))
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")


#같은 학교 같은 학년 같은 반 같은 수업
# def profile(name,age=17,main_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
#     .format(name,age,main_lang))

# profile("유재석")
# profile("김태호")

############################키워드값
# def profile(name,age,main_lang):
#     print(name,age,main_lang)
# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="자바",name="김태호",age=25)


############################가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# def profile(name,age,*language):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     for lang in language:
#         print(lang,end=" ")
#     print()

# profile("유재석",20,"python","java","c","c++","c#","javascript")
# profile("김태호",25,"Kotlin","swift")

##################지역변수와 전역변수
# gun=10

# # def checkpoint(soldiers):
# #     global gun #전역 공간에 있는 gun사용
# #     gun=gun-soldiers
# #     print("[함수 내] 남은 총: {0}".format(gun))
# def checkpoint_ret(gun,soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun
# print("전체: {0}".format(gun))
# gun=checkpoint_ret(gun,2)
# print("남은 총: {0}".format(gun))

########################표준 체중 구하는 프로그램 퀴즈

# def std_weight(height,gender):
#     m_height=height/100
#     if gender=="여자":
#         weight=round(m_height*m_height*21,2)
#     else:
#         weight=round(m_height*m_height*22,2)  
#     print("키 {0} {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))  
# std_weight(175,"남자")

##########################표준입출력
# import sys 
# print("python","java",file=sys.stdout)
# print("python","java",file=sys.stderr)

# scores={"수학":0,"영어":50,"코딩":100}
# for subject,score in scores.items():
#    # print(subject,score)
#    print(subject.ljust(8),str(score).rjust(4),sep=":")

#은행대기 순번표
#001,002,003...
# for num in range(1,21):
#     print("대기번호:"+str(num).zfill(3)) #0으로 채우기

# answer=input("아무 값이나 입력하세요: ")##########항상 문자열형태로 저장된다.
# print(answer,type(answer))
# print("입력하신 값은 "+answer+"입니다.")

#####################다양한 출력 포맷

#빈 자리는 빈공간으로 두고,오른쪽 정렬을 하되, 총 10 공간을 확보
# print("{0: >10}".format(500))

# #양수일 때는 +표시, 음수일 때는 -표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))


# #왼쪽 정렬,빈칸은 _로 채움
# print("{0:_<+10}".format(500))

# #세자리 마다 콤마
# print("{0:,}".format(10000000000000))
# #세자리 마다 콤마,+,-부호
# print("{0:+,}".format(10000000000000))
# #세자리 마다 콤마,+,-부호,자리수도 확보,돈이 많으면 행복하니깐 빈자리는 ^
# print("{0:^<+30,}".format(100000000000000))
# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리수까지
# print("{0:.2f}".format(5/3))


##############파일 입출력
# score_file=open("score.txt","w",encoding="utf8")
# print("수학:0",file=score_file)
# print("영어:50",file=score_file)
# score_file.close()

# score_file=open("score.txt","a",encoding="utf8")
# score_file.write("과학:80")
# score_file.write("\n코딩:100")
# score_file.close()


# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="") #줄별로 읽기,한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# lines=score_file.readlines()
# for line in lines:
#     print(line,end="")
# score_file.close()


#################pickle
# import pickle
# profile_file=open("profile.pickle","wb")
# profile={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)   #profile에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file=open("profile.pickle","rb")
# profile=pickle.load(profile_file)#file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


#################with
# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())


##################file퀴즈
# for i in range(1,51): 
#     with open("{0}주차.txt".format(i),"w",encoding="utf8") as report:
#         report.write("-{0} 주차 주간보고- \n부서:\n이름:\n업무요약:".format(i) )
         
######################클래스
#마린:공격유닛,군인,총을 쏨
# name="마린"
# hp=40#체력
# damage=5#공격력
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0},공격력 {1}\n".format(hp,damage))

# #탱크:일반/시즈모드
# tank_name="탱크"
# tank_hp=150
# tank_damage=35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0},공격력 {1}\n".format(tank_hp,tank_damage))

# tank_name2="탱크2"
# tank_hp2=150
# tank_damage2=35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0},공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]".format(\
#         name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank_name2,"1시",tank_damage2)

# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0},공격력 {1}".format(self.hp,self.damage))

# marine1=Unit("마린",40,5)
# marine2=Unit("마린",40,5)
# tank=Unit("탱크",150,35)

#####################멤버변수

# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0},공격력 {1}".format(self.hp,self.damage))


# wraith1=Unit("레이스",80,5)
# print("유닛이름: {0}, 공격력: {1}".format(wraith1.name,wraith1.damage))
# #마인드 컨트롤:상대방 유닛을 내것으로 만드는 것(빼앗음)
# wraith2=Unit("레이스",80,5)
# wraith2.clocking=True

# if wraith2.clocking==True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#######3메소드
# class AttackUnit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
    
#     def attack(self,location):
#          print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
#              .format(self.name,location,self.damage))

#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}:현재체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다.".format(self.name))

# firebat1=AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


###########상속

# class Unit:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp

# class AttackUnit(Unit):
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage=damage
    
#     def attack(self,location):
#          print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
#              .format(self.name,location,self.damage))

#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}:현재체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다.".format(self.name))

# firebat1=AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

###########다중상속

# class Unit:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp

# class AttackUnit(Unit):
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage=damage
    
#     def attack(self,location):
#          print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
#              .format(self.name,location,self.damage))

#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}:현재체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다.".format(self.name))
# class Flyable:
#     def __init__(self,speed):
#         self.speed=speed
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location,self.speed))

# class FlyalbeAttackUnit(AttackUnit,Flyable):
#     def __init__(self,name,hp,damage,speed):
#         AttackUnit.__init__(self,name,hp,damage)
#         Flyable.__init__(self,speed)

# valkyrie=FlyalbeAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")



###########메소드 오버라이딩
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name=name
#         self.hp=hp
#         self.speed=speed
#     def move(self,location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name,location,self.speed))

# class AttackUnit(Unit):
#     def __init__(self,name,hp,speed,damage):
#         Unit.__init__(self,name,hp,speed)
#         self.damage=damage
    
#     def attack(self,location):
#          print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
#              .format(self.name,location,self.damage))

#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}:현재체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다.".format(self.name))
# class Flyable:
#     def __init__(self,speed):
#         self.speed=speed
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location,self.speed))

# class FlyalbeAttackUnit(AttackUnit,Flyable):
#     def __init__(self,name,hp,damage,speed):
#         AttackUnit.__init__(self,name,hp,0,damage)
#         Flyable.__init__(self,speed)
#     def move(self,location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location)
# vulture=AttackUnit("벌쳐",80,10,20)
# battlecruiser=FlyalbeAttackUnit("배틀그루져",500,25,3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name,"9시")
# battlecruiser.move("9시")

###############pass
#건물
# class buildingUnit(Unit):
#     def __init__(self,name,hp,location):
#         pass

# supply_depot=buildingUnit("서플라이 디폿",500,"7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass
# game_start()
# game_over()


###############super
# class Unit:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp

# class buildingUnit(Unit):
#     def __init__(self,name,hp,location):
#         #Unit.__init__(self,name,hp,0)
#         super().__init__(name,hp,0)
#         self.location=location


##################스타그래프트 전반전
#일반 유닛
# from random import *
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name=name
#         self.hp=hp
#         self.speed=speed
#         print("{0} 유닛이 생성되었습니다.".format(self.name))

#     def move(self,location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name,location,self.speed))

#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}:현재체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다.".format(self.name))
# #공격 유닛
# class AttackUnit(Unit):
#     def __init__(self,name,hp,speed,damage):
#         Unit.__init__(self,name,hp,speed)
#         self.damage=damage
    
#     def attack(self,location):
#          print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
#              .format(self.name,location,self.damage))

#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}:현재체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다.".format(self.name))
# #마린
# class Marine(AttackUnit):
#     def  __init__(self):
#         AttackUnit.__init__(self,"마린",40,1,5)

#     def stimpack(self):
#         if self.hp>10:
#             self.hp-=10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
# #탱크
# class Tank(AttackUnit):
#     seize_developed=False

#     def  __init__(self):
#         AttackUnit.__init__(self,"탱크",150,1,35)
#         self.seize_mode=False

#     def set_seize_mode(self):
#         if Tank.seize_developed==False:
#             return
        
#         if self.seize_mode==False:
#             print("{0}: 시즈모드로 전환합니다.".format(self.name))
#             self.damage*=2
#             self.seize_mode=True
#         else:
#             print("{0}: 시즈모드를 해제합니다.".format(self.name))
#             self.damage/=2
#             self.seize_mode=False



# class Flyable:
#     def __init__(self,speed):
#         self.speed=speed
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location,self.speed))

# class FlyalbeAttackUnit(AttackUnit,Flyable):
#     def __init__(self,name,hp,damage,speed):
#         AttackUnit.__init__(self,name,hp,0,damage)
#         Flyable.__init__(self,speed)
#     def move(self,location):
#         self.fly(self.name,location)

# #레이스
# class Wraith(FlyalbeAttackUnit):
#     def __init__(self):
#         FlyalbeAttackUnit.__init__(self,"레이스",80,20,5)
#         self.clocked=False

#     def clocking(self):
#         if self.clocked ==True:
#             print("{0}: 클로킹모드로 해제합니다.".format(self.name))
#             self.clocked=False

#         else:
#             print("{0}: 클로킹모드로 성정합니다.".format(self.name))
#             self.clocked=True

# def game_start():
#     print("[알림] 새로운 게임이 시작되었습니다.")
# def game_over():
#     print("Player:gg")
#     print("[Player]님이 게임에서 퇴장하셨습니다.")

# game_start()

# m1=Marine()
# m2=Marine()
# m3=Marine()

# t1=Tank()
# t2=Tank()

# w1=Wraith()

# attack_unit=[]
# attack_unit.append(m1)
# attack_unit.append(m2)
# attack_unit.append(m3)
# attack_unit.append(t1)
# attack_unit.append(t2)
# attack_unit.append(w1)

# for Unit in attack_unit:
#     Unit.move("1시")
 
# Tank.seize_developed=True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# for Unit in attack_unit:
#     if isinstance(Unit,Marine):
#         Unit.stimpack()
#     elif isinstance(Unit,Tank):
#         Unit.set_seize_mode()
#     elif isinstance(Unit,Wraith):
#         Unit.clocking()

# for Unit in attack_unit:
#     Unit.attack("1시")

# for Unit in attack_unit:
#     Unit.damaged(randint(5,21))

# game_over()

###################클래스 프로그램 퀴즈
# class House:
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.completion_year=completion_year
#     def show_detail(self):
#         print(self.location,self.house_type,self.deal_type\
#             ,self.price,self.completion_year)
# house=[]
# house1=House("강남","아파트","매매","10억","2010년")       
# house2=House("마포","오피스텔","전세","5억","2007년")   
# house3=House("송파","빌라","월세","500/50","2000년")   
# house.append(house1)
# house.append(house2)
# house.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(house)))

# for i in house:
#     i.show_detail()




###################예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums=[]
#     nums.append(int(input("첫번째 숫자를 입력하세요")))
#     nums.append(int(input("두번째 숫자를 입력하세요")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[1],nums[2],nums[2]))
# except ValueError:
#     print("에러가 발생하였습니다.")

# except ZeroDivisionError as err:
#     print(err)

# except: #####위의 두 예외를 제외한 에러
#     print("알 수 없는 오류가 발생하였습니다.")




###################에러발생 시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1=int((input("첫번째 숫자를 입력하세요:")))
#     num2=int((input("두번째 숫자를 입력하세요:")))
#     if(num1>=10 or num2 >= 10):
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

###################사용자 전용 에러 발생
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1=int((input("첫번째 숫자를 입력하세요:")))
#     num2=int((input("두번째 숫자를 입력하세요:")))
#     if(num1>=10 or num2 >= 10):
#         raise BigNumberError("입력값: {0}, {1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)



###################finally
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1=int((input("첫번째 숫자를 입력하세요:")))
#     num2=int((input("두번째 숫자를 입력하세요:")))
#     if(num1>=10 or num2 >= 10):
#         raise BigNumberError("입력값: {0}, {1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:############예외와 상관없이 항상 출력
#     print("계산기를 이용해 주셔서 감사합니다.")


###################치킨집 예외처리 퀴즈
# class SoldOutError(Exception):
#     pass
# chicken=10
# waiting=1
# while(True):
#     try:
#         print("[남은 치킨: {0}]".format(chicken))
#         order= int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif(order <1):
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting,order))
#             waiting+=1
#             chicken-=order
#         if (chicken==0):
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")

#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break


###################모듈
# import theater_module
# theater_module.price(3) #3명이 영화보러 갔을 때 가격
# theater_module.price_morning(4) #4명이 조조 영화보러 갔을 때 가격
# theater_module.price_soldier(5) #5명의 군인이 영화보러 갔을 때 가격

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price,price_morning
# price(5)
# price_morning(4)


# from theater_module import price_soldier as price
# price(5)

#####################패키지
# import travel.Thailand
# # from travel.Thailand import ThailandPackage
# # trip_to=ThailandPackage
# trip_to=travel.Thailand.ThailandPackage()
# trip_to.detail()

# import travel.Vietnam
# trip_to=travel.Vietnam.VietnamPackage()
# trip_to.detail()


#####################__all__
# from travel import *
# # # trip_to=Vietnam.VietnamPackage()
# # trip_to=Thailand.ThailandPackage()
# # trip_to.detail()

# ###############패키지,모듈 위치 확인
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(Thailand))

######################내장 함수
#input:사용자 입력을 받는 함수
# language= input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다. ".format(language))

# #dir:어떤 객체를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst=[1,2,3]
# print(dir(lst))

# name="jin"
# print(dir(name))


######################외장 함수
#glob:경로 내의 파일 / 폴더 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))

#os:운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder="sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print("폴더가 삭제되었습니다.")
# else:
#     os.makedirs(folder)
#     print(folder,"폴더를 생성하였습니다.")

#time:시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ",datetime.date.today())

#timedelta:두 날짜 사이의 간격
# today=datetime.date.today()
# td=datetime.timedelta(days=100)
# print("우리가 만난지 100일은",today+td)


###############모듈 만들기 퀴즈
# import byme
# byme.sign()
