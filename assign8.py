a = int(input("Enter first number: "))
b = int(input("Entr second number: "))

if(a>b):
    greater = a

else:
    greater = b

while True :
    if(greater%a ==0 and greater%b == 0):
        lcm = greater 
        break
    greater += 1


print(f"LCM of {a} and {b} is: {lcm}")