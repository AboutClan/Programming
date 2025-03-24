N = int(input())  # 몇(N)번째 영화 제목을 구할건지 입력
count = 0         # 찾은 666 개수, 처음엔 0으로 시
num = 666         # 666부터 시작 666,1666,2666...

while True: #조건 없이 계속 반복, break로 종료. 
    if '666' in str(num):  # 숫자에 '666'이 포함되면
        count += 1         # 찾은 개수 +1
        if count == N:     # N번째면 출력하고 끝
            print(num)
            break
    num += 1  #  n번째 될때까지 다음 숫자로 넘어감
