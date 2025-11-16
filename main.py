def password_checker():
    should_continue = True
    while should_continue:

        password = input("Enter your password: ")

        # Security Checks
        symbol = "!@#$%^&*())_+}{|:?><~=-[];./,`'"
        #  Placeholders
        check_length    = False
        check_digit     = False
        check_lower     = False
        check_upper     = False
        check_symbol    = False
        check_space     = False
        # Length minimum of 8 letters
        if len(password) >= 8:
            check_length = True
        #  Contains space
        if " " not in password:  # Used if there is space in the password
            check_space = True
        for char in password:
            #  Contains at least one digit
            if char.isdigit():
                check_digit = True
            #  Contains at least one lowercase letter
            elif char.islower():
                check_lower = True
            #  Contains at least one uppercase letter
            elif char.isupper():
                check_upper = True
            #  Contains at least one digit
            elif char in symbol:
                check_symbol = True
        #  Display results
        check =[
            check_length,
            check_digit,
            check_lower,
            check_upper,
            check_symbol,
            check_space,
        ]
        if all(check):
            # (check_length and check_digit and check_lower
            # and check_upper and check_symbol and check_space)
            should_continue = False
            print("Password is strong enough, you can use it.")
        else:
            print("Password is not strong enough")

            if not check_length:
                print("Password must be at least 8 characters long")
            if not check_digit:
                print("Password must contain at least one digit")
            if not check_lower:
                print("Password must contain at least one lowercase letter")
            if not check_upper:
                print("Password must contain at least one uppercase letter")
            if not check_symbol:
                print(f"Password must contain at least one symbol ({symbol})")
            if not check_space:
                print("Password must not contain any space")

password_checker()