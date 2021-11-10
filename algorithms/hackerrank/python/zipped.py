n, x = map(int, input().split())

scores = []
for _ in range(x):
    score = list(map(float, input().split()))
    scores.append(score)

z = zip(*scores)
for score in z:
    print(sum(score) / x)
