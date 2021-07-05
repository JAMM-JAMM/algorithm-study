# 문제
# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할
# 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# 아이디어
# '가장 큰 화폐 단위부터' 돈을 거슬러 주는 것

money = int(input())

coin_count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    temp = money // coin # money를 coin으로 나눈 몫
    coin_count += temp
    money %= coin # money의 값을 coin으로 나눈 나머지로 바꿔준다.
    print("{}원 {}개".format(coin, temp))

print("거슬러줘야 할 동전의 최소 개수 {}".format(coin_count))