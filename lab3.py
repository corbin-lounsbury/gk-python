# Instructions
# 1. Create an if statement that checks whether a user is logged in and is a Gold Member
# 2. If the user is logged in, print "User is logged in".
# 3. If the user is lagged in and is a Gold Member, print "Welcome Gold Member!".
# 4. If the user is not logged in and is a Gold Member, print "Please log in, Gold Member".
# 5. If the user is not logged in, print "Please log in".
# 6. Test for the user that is not logged in and is a Gold Member.

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
