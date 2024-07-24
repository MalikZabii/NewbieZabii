height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
bmi_in_int = int(bmi)
print("Your BMI is " + str(bmi_in_int))



