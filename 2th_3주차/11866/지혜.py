n, k = map(int, input().split())

people = []
for i in range(1, n + 1):
    people.append(i)

result = []

index = 0

while len(people) > 0:
    index = index + (k - 1)

    if index >= len(people):
        index = index % len(people)

    result.append(people[index])
    del people[index]

print("<", end="")

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end="")
    else:
        print(result[i], end=", ")

print(">")
