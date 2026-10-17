str = input()
rev = ""
for i in range(len(str)-1, -1, -1):
    rev += str[i]

if(str == rev):
    print("Palindrome")
else:
    print("Not Palindrome")