number= input().split('-') #################################55-(50+40)-(60+40) -를 기준으로 괄호를 생성하였을 때 가장 최소값
answer=sum(list(map(int,number[0].split('+'))))
for i in range(1,len(number)):
    answer-=sum(list(map(int,number[i].split('+'))))
print(answer)


