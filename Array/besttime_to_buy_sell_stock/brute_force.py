from typing import List

class Test:
   def maxProfit(self,prices:List[int])->int:
       max_price=0
       for i,price in enumerate(prices):
           for j in range(i,len(prices)):
               max_price=max(prices[j]-price,max_price)
       return max_price
   
w1=Test()
print(w1.maxProfit(prices=[7,1,5,3,6,4]))
