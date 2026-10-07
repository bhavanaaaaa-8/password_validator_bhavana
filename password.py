password = input("Enter your password: ")
has_upper = False
has_lower = False
has_number = False
has_special = False
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_number = True
    elif char in "!@#$%^&*~":
        has_special = True
if len(password) < 8:
    print("Invalid: Password must contain at least 8 characters.")
if not has_upper:
    print("Invalid: Password must contain at least one uppercase letter.")
if not has_lower:
    print("Invalid: Password must contain at least one lowercase letter.")
if not has_number:
    print("Invalid: Password must contain at least one number.")
if not has_special:
    print("Invalid: Password must contain at least one special character.")
if len(password) >= 8 and has_upper and has_lower and has_number and has_special:
    print("Valid: Password meets all basic requirements.")
