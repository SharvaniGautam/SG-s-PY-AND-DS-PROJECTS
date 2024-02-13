email = input("Enter your Email : ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):  # corrected XOR to OR
                for i in email:
                    if i.isspace():  # corrected condition to check if a character is space
                        k = 1
                    elif i.isalpha():  # corrected isaplha() to isalpha()
                        if i.isupper():  # corrected isaplha() to isalpha()
                            j = 1
                        elif i.isdigit() or i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Valid Email")
                else:
                    print("Wrong Email 4")
            else:
                print("Wrong Email 3")
        else:
            print("Wrong Email 2")
    else:
        print("Wrong Email 1")
else:
    print("Wrong Email 5")
