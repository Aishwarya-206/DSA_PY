n = int(input("size: "))
arr = list(map(int, input().split()))
freq ={}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
maxf = 0
num = None
for key, value in freq.items():
    if(value>maxf):
        maxf = value
        num = key

print(num)