def 기준(x):
    return (len(x), x)  # 길이 먼저, 알파벳 순서 다음

N = int(input())    
words = []         

for _ in range(N):
    word = input()
    if word not in words: 
        words.append(word)

words.sort(key=기준) 

for w in words:
    print(w)
