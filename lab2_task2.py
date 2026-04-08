list1=[]
print("Enter values of first list:")
for i in range(5):
    val=input("Enter value:")
    n=int(val)
    list1.append(n)

list2=[]
print("Enter values of second list:")
for i in range(5):
    val=input("Enter value:")
    n=int(val)
    list2.append(n)

list3=list1+list2
list3.sort()
print(list3)

print("Smallest number in list 3 is:",list3[0])
print("Largest number in list 3 is:",list3[-1])   