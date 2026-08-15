H, M = map(int, input().split())

def increment_time(h:int, m:int):
    return ((h + ((m + 1) // 60)) % 24, (m + 1) % 60)

def correct_time(h:int, m:int):
    return 0 <= h <= 23 and 0 <= m <= 59

def inverse_time(h:int, m:int):
    return (h // 10 * 10 + m // 10, h % 10 * 10 + m % 10)

h, m = H, M

while True:
    if correct_time(*inverse_time(h, m)):
        print(h, m)
        exit()
    h, m = increment_time(h, m)

