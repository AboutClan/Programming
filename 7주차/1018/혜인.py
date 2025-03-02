N,M = map(int, input().split())
board = []
result = []
for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        change1 = 0
        change2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 ==0:
                    if board[a][b] != 'B':
                        change1 += 1
                    if board[a][b] != 'W':
                        change2 += 1
                else:
                    if board[a][b] != 'W':
                        change1 += 1
                    if board[a][b] != 'B':
                        change2 += 1
        result.append(change1)
        result.append(change2)

print(min(result))