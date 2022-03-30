input_data = input()

col = int(input_data[1])
row = int(ord(input_data[0])) - 96

# 8가지 경우의 수 (x, y)
steps = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

count = 0
for i in steps:
    nc = col + i[0]
    nr = row + i[1]
    if 1 <= nc <= 8 and 1 <= nr <= 8:
        count += 1

print(count)