a = int(input())
b = list(map(int, input().split()))

sort = sorted(list(set(b)))
dic = {sort[x]: x for x in range(len(sort))}
print(*[dic.get(a) for a in b])

# # 디버깅용
# import random
# b = [random.randrange(-10**9, 10**9) for a in range(1000000)]
# a = len(b)

# sort = sorted(list(set(b)))
# dic = {sort[x]: x for x in range(len(sort))}
# print(*[dic.get(a) for a in b])

