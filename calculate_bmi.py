def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "insufficient body weight(underweight)"
    elif 18.5 <= bmi < 24.9:
        return "normal body weight"
    elif 25 <= bmi < 29.9:
        return "overweight(obesity)"
    else:
        return "adiposity"


try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    bmi = calculate_bmi(weight, height)
    print(bmi)
    print(f"Your body mass index (BMI) is: {bmi}")
    print("Your state of health: " + interpret_bmi(bmi))

except ValueError:
    print("You have entered incorrect data. Please enter numerical values for weight and height.")