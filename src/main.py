from bmi import calculate_bmi
from bmr import calculate_bmr

print("\n-------------Welcome Fitness Calculator--------------")
print("\n--------------Enter Your Choice----------------------")
print("\n                  1.  BMI                            ")
print("\n                  2.  BMR                            ")
print("\n                  3.  EXIT                           ")
choice = int(input().strip())
if choice == 1:
    calculate_bmi()
elif choice == 2:
    calculate_bmr()
else:
    quit()
