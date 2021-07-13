number,total= map(int, input().strip().split(' '))
num_list=[]
for i in range(number):
    value=int(input())
    if value<=total:
        num_list.append(value)
num_list=sorted(num_list,reverse=True)
count=0
for money in range(len(num_list)):
    count+=total//num_list[money]
    total=total%num_list[money]
print(count)



