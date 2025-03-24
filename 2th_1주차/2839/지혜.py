N = int(input())  # 총 설탕 무게 입력

count = 0  # 봉지 개수

# 큰 봉지(5kg)를 최대한 쓰고, 남는거 3kg
while N >= 0: #봉지로 정확히 나눠지면 계속, 안되면 else
    if N % 5 == 0:         # 5kg 봉지로 정확히 나눠지면
        count += N // 5    # 무게/5 만큼 봉지 추가
        print(count)
        break
    N -= 3                # 5kg로 안 되면 3kg 봉지를 하나 써서 남은 무게 - 3kg
    count += 1            # 3kg 봉지를 하나 썼으니 봉지 개수 +1
else:
    print(-1)             # 정확하게 Nkg을 나눌수 없으면 -1 출력
