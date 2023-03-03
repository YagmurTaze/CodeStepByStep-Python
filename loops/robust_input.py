while True:
    try:
        age = int(input("Type your age: "))
        break
    except:
        pass
while True:
    try:
        gpa = float(input("Type your GPA: "))
        break
    except:
        pass
print("age =",age," GPA =",gpa)
