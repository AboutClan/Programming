# 입력 받기
N, M = map(int, input().split()) #첫째 줄에 N행 M열인 보드 입력
board = [input() for _ in range(N)] #보드를 한 줄씩 받아서 리스트에 저장

min_count = 64  # 최대 64칸. 최대값으로 시작해서 나중에 더 적은 칸으로 바꾸면 그걸 저장

for i in range(N - 7):       # 위에서 아로, 세로 시작점 i
    for j in range(M - 7):   # 왼 -> 오 가로 시작점 j #i, j는 8×8 체스판의 시작 위치
        white_start = 0  # 왼쪽 위가 'W'일 때 다시 칠할 칸 수
        black_start = 0  # 왼쪽 위가 'B'일 때 다시 칠할 칸 수
        
        for x in range(8): #8*8 체스판의 행, 열을 순회
            for y in range(8):
                current = board[i + x][j + y] #현재 검사중인 보드칸
                if (x + y) % 2 == 0: # 짝수 칸만 검사: (x+y)가 짝수(0, 2, 4...)일 땐 시작 색과 같아야 함
                    if current != 'W': #현재 W가 아니면
                        white_start += 1 #white_start에 1을 더해(다시 칠해야 하니까)
                    if current != 'B': #현재 B가 아니면
                        black_start += 1 #black_start에 1을 더해
                else: #홀수 칸(1, 3 ...)일땐 시작색과 다름
                    if current != 'B': #그래서 반대로 카운트 더
                        white_start += 1
                    if current != 'W':
                        black_start += 1

        min_count = min(min_count, white_start, black_start) #최솟값 저장

print(min_count)
