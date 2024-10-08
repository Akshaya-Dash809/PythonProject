height = int(input("Enter your height in feet : "))

if height >= 3 :
    print("Can Ride")
    age = int(input("Enter your age in years : "))
    if age < 12 :
        print("Please pay rs150")
    elif age <= 18 :
        print("Please pay rs250")
    else :
        print("Please pay rs500")
else:
    print ("Can't Ride")

print("Bye Visit Again!!!!!")