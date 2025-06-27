import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("Add lowercase letters.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("Add uppercase letters.")

    # Digit check
    if re.search(r'[0-9]', password):
        strength_points += 1
    else:
        feedback.append("Add digits.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_points += 1
    else:
        feedback.append("Add special characters.")

    # Evaluate strength level
    if strength_points == 5:
        strength = "Very Strong"
    elif strength_points == 4:
        strength = "Strong"
    elif strength_points == 3:
        strength = "Moderate"
    elif strength_points == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def main():
    password = input("Enter your password to check strength: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(" -", tip)
    else:
        print("Great password!")

if __name__ == "__main__":
    main()
