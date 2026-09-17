weight = float(input())
height = float(input())
bmi = weight / height / height
if bmi >= 25:
    print("Overweight")
    print("You should do more exercise")
elif bmi < 18.5:
    print("Underweight")
    print("Please eat more")
else:
    print("Normal")
    print("Good!")