username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "pass":
    print("Login successful!")
else:
    if username != "admin":
        print("Invalid username.")
    else:
        print("Invalid password.")