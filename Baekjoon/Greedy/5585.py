money=int(input())
result_money=1000-money
rest=[500, 100, 50, 10, 5, 1]
count=0
for i in rest:
    if result_money>=i:
        count += result_money // i
        result_money=result_money%i
print(count)
