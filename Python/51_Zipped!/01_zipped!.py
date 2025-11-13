# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
marks = []
for _ in range(X):
    marks.append(list(map(float, input().split())))
marks = list(zip(*marks))
for i in range(N):
    print(sum(marks[i])/X)
