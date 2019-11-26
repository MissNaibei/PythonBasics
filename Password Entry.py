
attempts = 3
password = 1234
while attempts < 3:
    password = input("Enter Password: ")
    print(password)

if password == 1234:
    print("Login Successful!")
else:
    print("Access Denied. Contact the administrator.")
