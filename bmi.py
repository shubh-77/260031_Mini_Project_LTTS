

def calculate_bmi():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    BMI = weight / (height/100)**2
    formatted_float_bmi = "{:.2f}".format(BMI)
    status = ""
    if BMI <= 18.4:
        status = "You are underweight."
    elif BMI <= 24.9:
        status = "You are healthy."
    elif BMI <= 29.9:
        status = "You are over weight."
    elif BMI <= 34.9:
        status = "You are severely over weight."
    elif BMI <= 39.9:
        status = "\nYou are obese."
    else:
        status = "You are severely obese."

    f = open("BMI-Report.txt", "w")
    f.write("\n----------------------------------------------------------------")
    f.write("\n| ###   #   #   ###     # #    # # #  # #   # # #  # #   ##### |")
    f.write("\n| #  #  # # #    #      #  #   #      #  #  #   #  #  #    #   |")
    f.write("\n| ####  # # #    #      ###    # # #  ###   #   #  ###     #   |")
    f.write("\n| #  #  #   #    #      #  #   #      #     #   #  #  #    #   |")
    f.write("\n| ###   #   #   ###     #   #  # # #  #     # # #  #   #   #   |")
    f.write("\n----------------------------------------------------------------")
    f.write("\n                                                                   ")
    f.write("\n1. WEIGHT:           |    " + str(weight)+"  kgs")
    f.write("\n2. HEIGHT:           |    " + str(height)+" cms")
    f.write("\n                                                                   ")
    f.write("\n----------------------------------------------------------------")
    f.write("\nYour Body Mass Index is: "+str(formatted_float_bmi))
    f.write("\nYour Health status: "+status)
    f.write("\n----------------------------------------------------------------")
    f.close()
