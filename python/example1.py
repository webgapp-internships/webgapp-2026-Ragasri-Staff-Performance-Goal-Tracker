print("sri")
password = ""
while  password != "sri":
 password = input("enter your password:")
print("Login Successfully")


subjects=["English","Tamil","Maths","Science","Social"]
total = 0
for i in subjects:
    mark = int(input("Enter mark for " + i + ": "))
    total=total + mark
    if mark >=95:
        grade = "O"
    elif mark >=90:
        grade = "A+"    
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "B+"
    elif mark >= 50:
        grade = "U"
    else:
        grade = "Fail"
    print( i, "Grade:", grade)
print("Total Marks",total)

if total>=250:
    print("Congrats")
else:
    print("Better Luck Next Time")    