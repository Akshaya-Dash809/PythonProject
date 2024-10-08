height = int(input("Enter your height in feets: "))
bill =0

if height > 3 :
    print("Can Ride")
    age = int(input("Enter your age in years: "))
    if age<12 :
        bill = 150
        print("Ticket price is rs150. ")
    if age <= 18 :
        bill= 250
        print("Ticket price is rs250. ")
    else:
        bill = 500
        print("Ticket price is rs500. ")

    want_photo = input("Do you want to take photo(Y/N)? ")
    if want_photo == "Y" or want_photo == "y":
        bill = bill + 50
    print("Your bill is",bill)
else:
    print("can't ride")

print("Bye Visit Again !!!!!!!!!!!!!!!!!!")
