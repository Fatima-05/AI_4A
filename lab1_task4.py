marks=int(input("Enter your marks:"))
if (marks>100 or marks<0):
    print("Marks must be between 0-100")
elif marks>90:
    print("Your grade is: A")
elif marks>80:
    print("Your grade is: B")
elif marks>70:
    print("Your grade is: C")
elif marks>60:
    print("Your grade is: D")
elif marks>=50:
    print("Your grade is: E")
else:
    print("Your grade is: F")