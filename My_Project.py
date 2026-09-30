print("Welcome to the Interactive Personal Data collector !")

Name=input("Please Enter Your Name :")
Age=int(input("Please Enter Your Age :"))
Height=float(input("Please Enter You Height in meters :"))
Fav=int(input("Please Enter Your Favourite Number :"))

age=2026-Age



print("Thank You ! Here is the information that we collect from you ")



print("Name :",Name,type(Name),"Memory Address :",id(Name))
print("Age :",Age,type(Age),"Memory Address :",id(Age))
print("Height :",Height,type(Height),"Memory Address :",id(Height))
print("Favourite Number :",Fav,type(Fav),"Memory Address :",id(Fav))

print("Your Birth Year is Approximately:",age,"(Based On Your Age)")


print("Thank You For Using Personal Data Collector")