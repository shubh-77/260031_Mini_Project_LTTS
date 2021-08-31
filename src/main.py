from bmi import calculate_bmi
from bmr import calculate_bmr

# Execution starts from here
print("\n-------------Welcome Fitness Calculator--------------")
print("\n--------------Enter Your Choice----------------------")
print("\n                  1.  BMI                            ")
print("\n                  2.  BMR                            ")
print("\n                  3.  EXIT                           ")
choice = int(input().strip())
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
if choice == 1:
    BMI = calculate_bmi(weight, height)
    print("BMI:"+str(BMI))
elif choice == 2:
    age = int(input("Enter your age in years: ").strip())
    gender = input("Are you male? (M/F): ").strip()
    BMR = calculate_bmr(weight, height, age, gender)
    print("BMR:"+str(BMR))
else:
    quit()
