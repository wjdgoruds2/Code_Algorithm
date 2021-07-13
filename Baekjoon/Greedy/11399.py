total = int(input())
number= list(map(int, input().strip().split(' ')))
number=sorted(number)
count=0
answer=0
for i in range(0,total):
    count=count+number[i]
    answer=answer+count
print(answer)
