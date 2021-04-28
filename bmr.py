# Basal Metabolic Rate Calculator
def calculate_bmr():
    weight = float(input("Enter your weight in KG: \n"))
    height = float(input("Enter your height in cm: \n"))
    age = int(input("Enter your age in years: \n"))
    gender = str(input("Are you male? (M/F)")).strip()

    # Mifflin St. Jeor Equation for male
    if gender == "M" or gender == "m":
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    elif gender == "F" or gender == "f":
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    else:
        print("Error")
        quit()

    bmr = round(bmr)
    f = open("BMR-Report.txt", "w")
    f.write("\n-------------------------------------------------------------------")
    f.write("\n| ###   #   #  # #         # #    # # #  # #   # # #  # #   ##### |")
    f.write("\n| #  #  # # #  #  #        #  #   #      #  #  #   #  #  #    #   |")
    f.write("\n| ####  # # #  ###         ###    # # #  ###   #   #  ###     #   |")
    f.write("\n| #  #  #   #  #  #        #  #   #      #     #   #  #  #    #   |")
    f.write("\n| ###   #   #  #   #       #   #  # # #  #     # # #  #   #   #   |")
    f.write("\n-------------------------------------------------------------------")
    f.write("\n                                                                   ")
    f.write("\n 1. WEIGHT:           | "+"              "+str(weight)+" kgs  ")
    f.write("\n 2. HEIGHT:           | "+"              "+str(height)+" cms")
    f.write("\n 3. AGE:              | "+"              "+str(age)+" years")
    f.write("\n 4. GENDER:           | "+"              "+str(gender)+"  ")
    f.write("\n                                                                   ")
    f.write("\n-------------------------------------------------------------------")
    f.write("\nYour Basal Metabolic Rate is:  "+str(bmr)+" calories/day      ")
    f.write("\n-------------------------------------------------------------------")
    f.close()
