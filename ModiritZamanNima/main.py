time = input().split()
w = int(time[0])
s = int(time[1])
i = int(time[2])

if i <= (s + w):
    result = w + s - i
    if result <= 24:
        print(24 - result)