# num=input("Enter any number:")
# rev_num="".join(reversed(num))
# print("Number in reverse is:",rev_num)


# I used the above logic earlier when you gave us the tasks in online class, below is the logic using lists as we learned today:

list=[]
num=input("Enter any number:")
for i in num:
    list.append(i)

rev_num=num[::-1]
print(rev_num)