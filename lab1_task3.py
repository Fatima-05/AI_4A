terms=input("Enter no. of terms to be displayed:")
first_term=0
second_term=1

if int(terms)<=0:
    print("Entered terms must be greater than 0")
else:
    for i in range(int(terms)):
        print(f"{first_term} ")
        temp=first_term+second_term
        first_term=second_term
        second_term=temp
        




