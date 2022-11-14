isLoggedIn = False
isGoldMember = True

print(f"User is logged in: {isLoggedIn}\nUser is gold member: {isGoldMember}")

if isLoggedIn == True:
    print("User is logged in")
    if isGoldMember == True:
        print("Welcome Gold Member!")
elif isLoggedIn == False:
    if isGoldMember == True:
        print("Please log in Gold Member")
    else:
        print("Please log in")
