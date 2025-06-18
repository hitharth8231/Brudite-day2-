#1
a = int(input("Enter a number"))
print (f"here is the input number {a}")

if a%3 == 0:
  if a%5 == 0:
    print("BRUDITE-NIRVANA")
  else:
    print("SKILLBREW")

if a%5 == 0:
  if a%3 == 0:
    print("BRUDITE-NIRVANA")
  else:
    print("BRUDITE")
     