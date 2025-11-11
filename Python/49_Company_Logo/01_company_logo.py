from collections import Counter
if __name__ == '__main__':
    s = input()
    count = dict(Counter(s))
    for i,j in sorted(count.items(), key=lambda x:(-x[1], x[0]))[:3]:
        print(i, j)
