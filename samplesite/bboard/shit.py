result = []
snail_map = [[1, 2, 3],
             [4,5,6],
             [7,8,9]]

n = len(snail_map)
p = 0
for i in range(n):
    for j in range(p, n-p):
        result.append(snail_map[i][j])
    for j in range(1+p, n - p):
        result.append(snail_map[j][n - 1 - p])
    for j in range(n-2-p, -1 + p, -1):
        result.append(snail_map[n - 1 - p][j])
    for j in range(n-2-p, p, -1):
        result.append(snail_map[j][p])

    p += 1

print(result)