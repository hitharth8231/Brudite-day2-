num = int(input("nums: "))
revnum = 0
while(num>0):
    digit = num%10
    revnum = revnum*10 + digit
    num= num//10

print(revnum)