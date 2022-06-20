def password_check(passwrd):
        is_valid=True
        only_letters_and_digits = True
        count_digits = 0
        if len(passwrd) < 6 or len(passwrd) > 10:
            print("Password must be between 6 and 10 characters")
            is_valid=False

        for el in passwrd:
            if el.isdigit():
                count_digits +=1
            if not el.isdigit() and not el.isalpha():
                only_letters_and_digits=False
                is_valid = False

        if not only_letters_and_digits:
            print("Password must consist only of letters and digits")
        if count_digits < 2:
            is_valid = False
            print("Password must have at least 2 digits")
        return  is_valid

password = input()
result = password_check(password)

if result:
    print("Password is valid")










password = input()
password_check(password)