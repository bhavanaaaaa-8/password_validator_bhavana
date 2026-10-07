# Password Validation Program
## Description
This Python program checks whether a password meets basic security requirements. It checks the password without displaying the actual password.

## Requirements
The password must contain:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (`!@#$%^&*`)

## How It Works
The program checks each character in the password using string methods such as:
- `.isupper()` – checks for uppercase letters
- `.islower()` – checks for lowercase letters
- `.isdigit()` – checks for numbers
- `len()` – checks the password length
It then displays clear validation messages for any requirements that are not satisfied.

## Example
```text
Enter your password: hello123

Invalid: Password must contain at least 8 characters.
Invalid: Password must contain at least one uppercase letter.
Invalid: Password must contain at least one special character.
```

If all requirements are satisfied:

```text
Valid: Password meets all basic requirements.
```

## Technologies Used
- Python
- String methods
- `for` loop
- `if` statements
