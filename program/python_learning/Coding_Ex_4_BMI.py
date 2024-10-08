# weight = 55
# height = 1.5
# bmi = weight // (height ** 2)
# print(bmi)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in mtr: "))

bmi = round(weight/height **2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are Underweight")
elif bmi<25 :
    print(f"Your BMI is {bmi} and you have a normal weight")
elif bmi<30 :
    print(f"Your BMI is {bmi} and you are Overweight")
elif bmi<35 :
    print(f"Your BMI is {bmi} and you are Obse. ")
else:
    print(f"Your BMI is {bmi} and you are clinically Obse. ")