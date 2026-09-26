from random import randint

print(3, 3)
for i in range(3):
    line = []
    for _ in range(3):
        line.append(randint(0, 1))
    print(*line)