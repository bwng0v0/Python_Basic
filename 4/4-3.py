x,y=input().split()
x=int(x)
y=int(y)

bmi = y/((x/100)**2)
if bmi<=18.5:
    print("Low Weight")
elif bmi<=23:
    print("Nomal")
elif bmi<=35:
    print("Over Weight")
elif bmi<=30:
    print("Obesity Level 1")
elif bmi<=35:
    print("Obesity Level 2")
elif bmi>35:
    print("Obesity Level 3")