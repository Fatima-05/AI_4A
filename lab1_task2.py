num=input("Enter a number:")
even_sum=0
odd_sum=0
for i in num:
    if int(i)%2==0:
        even_sum+=int(i)
    else:
        odd_sum+=int(i)

print("Sum of even digits in the number is:",even_sum)
print("Sum of odd digits in the number is:",odd_sum)