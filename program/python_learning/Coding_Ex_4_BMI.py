# weight = 55
# height = 1.5
# bmi = weight // (height ** 2)
# print(bmi)

weight = input("Enter your weight in kg: ")
height = input("Enter your height in mtr: ")

bmi = int(weight)/(float(height))**2
print("Your BMI is ", int(bmi))