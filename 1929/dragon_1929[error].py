import math

a, b = map(int, input().split())

def prime(i):
    for a in range(2, int(math.sqrt(i)) + 1):
        if i % a == 0:
            return False
    return True

before = [False for x in range(b+1)]

last = 0
count = 1
    
while len(before)-1 > count:
    count += 1
    if prime(count):
        before[count] = True
    
after = [x for x, y in enumerate(before) if x > a and y==True]

for i in after:
    print(i)


# 백준은 80% 정도 돌리다가 틀렸다고 하는데... 뭐에서 틀려먹는지 이유를 모름