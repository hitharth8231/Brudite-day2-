phy = int(input("enter physics number:"))
chem = int(input("enter chemistry number:"))
maths = int(input("enter maths number:"))
bio = int(input("enter biology number:"))
comp = int(input("enter computer number:"))

grade = phy+chem+maths+bio+comp 
perc = grade*0.2

if(perc >= 90):
    print("Grade A")

if(90 > perc >= 80):
    print("Grade B")

if(80 > perc >= 70):
    print("Grade C")

if(70 > perc >= 60):
    print("Grade D")

if(60 > perc >= 40):
    print("Grade E")

if(perc < 40):
    print("Grade F")