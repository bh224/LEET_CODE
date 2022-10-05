"""
121. Best Time to Buy and Sell Stock
한 번의 거래로 낼 수 있는 최대 이익 산출하기

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

리스트 안의 값은 [i]번째 날짜의 가격이다
리스트 안 어느 하나의 값을 선택해서 구입할 수 있고, 그 외 하나의 값을 선택해서 팔 수 있는데 
구입한 날보다 미래의 날짜를 선택해야한다

ex) prices[1] 번째 값에 구입했다면, 팔 수 있는 날짜는 [2]이상 이어야 한다

"""
#1 내가 푼 방법...^^

"""
1.  저점 = 가격리스트의 [0]번째 값으로 저장 (맨 처음 가격으로는 팔 수 없어서 설정함. 0보다 왼쪽에 있는 인덱스는 없으니까..)
* [0]번째 요소는 고점이 될 수 없고, [-1]번째 요소는 저점이 될 수없다.
2. [i]요소부터 꺼내서 현재 저점을 빼준다 (수익계산)
3. 2번의 차익이 현재 차익보다 크면 현재 차익을 교체한다
3-1. 2번의 차익이 현재 차익보다 작으면 현재 저점과 비교 후 [i]번째 값이 작으면 저점을 교체한다

** 
풀이처럼 아예 엄청 큰 값을 넣었으면 단순히 저점가격만 비교해도 됐을 텐데..
처음에 저점을 리스트의 첫번째 값으로 잡아버려서 식이 복잡해 진 것 같당
"""
prices = [7,1,5,3,6,4]

profit = 0
min_price = prices[0]

for price in prices:
    new_profit = price - min_price
    if new_profit > profit:
        profit = new_profit
    else:
        if price < min_price:
            min_price = price

#2 
import sys

prices = [7,1,5,3,6,4]
profit = 0
min_price = sys.maxsize # 설정할 수 있는 가장 큰값을 설정해 준다

for price in prices:
    min_price = min(min_price, price) #가격을 하나씩 가져와서 저점을 저장해준다
    profit = max(profit, price - min_price) 

print(profit)