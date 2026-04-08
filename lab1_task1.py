# num=input("Enter any number:")
# rev_num="".join(reversed(num))
# print("Number in reverse is:",rev_num)

list=[]
num=input("Enter any number:")
for i in num:
    list.append(i)

rev_num=num[::-1]
print(rev_num)