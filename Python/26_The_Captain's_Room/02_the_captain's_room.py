from collections import Counter
k = int(input())
room_no = Counter(list(map(int, input().split())))
for i in room_no:
    if room_no[i] == 1:
        print(i)
        break
