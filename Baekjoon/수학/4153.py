# 직각삼각형

result = []

while True:
    nums = list(map(int, input().split()))
    nums.sort()

    if nums[0] == 0:
        break

    if nums[2] ** 2 == nums[0]**2 + nums[1]**2:
        result.append("right")
    else:
        result.append("wrong")

for i in result:
    print(i)