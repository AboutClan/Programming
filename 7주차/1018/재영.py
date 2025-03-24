N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
chess = ['WBWBWBWB', 'BWBWBWBW']
count = []
for a in range(N-7):
    for b in range(M-7):
        chess_W = 0
        chess_B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if board[i][j] != chess[i%2][j-b]: chess_W += 1
                if board[i][j] != chess[(i+1)%2][j-b]: chess_B += 1
        count.append(chess_W)
        count.append(chess_B)
print(min(count))