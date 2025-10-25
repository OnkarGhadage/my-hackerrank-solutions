k = int(input())
room_no = list(map(int, input().split()))
rooms_dict = {}
for i in room_no:
    if i in rooms_dict:
        rooms_dict[i] += 1 
    else:
        rooms_dict[i] = 1
for i in rooms_dict:
    if rooms_dict[i] == 1:
        print(i)
        break
