# if_elif_else_statement.py

try:
    # 1. Prompt the user for their numeric grade.
    user_input = input("Enter your numeric grade: ")

    # 2. Convert the input string to an integer.
    grade = int(user_input)

    # 3. Determine the letter grade using if...elif...else.
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # 4. Print the result.
    print("Your grade is:", letter_grade)

except ValueError:
    # This block handles the case where the user does not enter a valid integer.
    print("Invalid input. Please enter an integer.")
