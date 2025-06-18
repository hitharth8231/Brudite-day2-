num = int(input("num: "))
while(num>10):
 list = [int(d) for d in str(num)]
 num = sum(list)

print(num)

