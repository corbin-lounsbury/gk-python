isLoggedIn = False
isGoldMember = True

if isLoggedIn == True:
    print("User is logged in")
    if isGoldMember == True:
        print("Welcome Gold Member!")
elif isLoggedIn == False:
    if isGoldMember == True:
        print("Please log in Gold Member")
    else:
        print("Please log in")
