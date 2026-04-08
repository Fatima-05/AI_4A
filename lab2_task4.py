birthdays={"Marwa":"31st August","Habiba":"30th May","Khola":"1st August","Sana":"6th August","Eman":"21st August", "Badami":"23rd December"}
print("Welcome to the birthday dictionary. We know the birthdays of:")
names=list(birthdays.keys())
for i in names:
    print(i)

search=input("Who's birthday do you want to look up? ")
res=birthdays.get(search)
if(res!=None):
    print(f"{search}'s brithday is on {birthdays[search]}")