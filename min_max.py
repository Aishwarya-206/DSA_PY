n = int(input("size: "))
arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]

for i in range(0, n):
    if(max<arr[i]):
        max = arr[i]
    if(min>arr[i]):
        min = arr[i]

print("max: ", max)
print("min: ", min)