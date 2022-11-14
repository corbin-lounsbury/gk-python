# Instructions
# 1. Create a program that determines your day's pay
# 2. Input the hourly rate and number of hours worked
# 3. Input a 40-hour work week at $60/hour

payRate = float(input("How much money per hour do you earn? : $"))
payHours = float(input("How many hours did you work? : "))

totalRate = payRate*payHours

print(f"You made ${totalRate:.2f} by working {payHours} hours and earning ${payRate:.2f} per hour")
