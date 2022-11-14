# instructions
# 1. Create a prgram that determines your day's pay
# 2. Input the hourly rate and number of hours worked
# 3. Input a 40-hour work week at $60/hour

payRate = int(input("How much money per hour do you earn? : $"))
payHours = int(input("How many hours did you work? : "))

totalRate = payRate*payHours

print(f"You made ${totalRate} by working {payHours} hours and earning ${payRate} per hour")
