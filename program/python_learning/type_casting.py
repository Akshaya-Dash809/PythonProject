# print(int("10"))
# print(int("10")+10)
# print(int("10")+int("10"))
# print(int("10")+float(10.6))
# print(str(10)+'10')
# print('my age is '+str(27))
#
# a=input('Input 1st number')
# b=input('Input 2nd number')
# c=a+b
# print(c) # It will print 1210 because input will always in string
# c=int(a)+int(b)
# print(c) # After type casting it'll print the sum as integer i.e. 30

####______________________PROGRAM____________________
number=input("Enter a two digit number: ")
_1st_digit = number[0] # store 1st digit to a variable
_2nd_digit = number[1] # store 2nd digit to a variable
print(int(_1st_digit)+int(_2nd_digit)) # add both digit by typecasting string to int

