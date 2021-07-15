import sys
alpha={'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
count=int(sys.stdin.readline())
total=0
compare=[]
for num in range(count):
    compare.append(input())
for i in compare:
    for j in range(len(i)):
        alpha[i[j]]+=10**(len(i)-j-1) ##################################십의 자리를 먼저 계산해서 입력
alpha=sorted(alpha.items(),key=lambda x: x[1],reverse=True) #####역순으로 정렬
for key in range(len(alpha)):
    if alpha[key][1]==0:
        break
    total+=(9-key)*alpha[key][1]
print(total)
