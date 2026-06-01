
password = input("Enter the password :")

if len(password)<6:
    print("weak pass")
elif len(password)<=10:
    print("medium pass")
else:
    print("strong pass")