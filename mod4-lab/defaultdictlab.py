# Instructions
# 1. Write a program to handle missing key exception in dictionary using different methods
# 2. Use setdefault method - to add a default value for a missing key 
# 3. Use get method
# 4. use if key in dict idiom
# 5. use try/except block of code 
# 6. finally use defaultdict
# 7. print the final result

from collections import defaultdict

def ifNoKey():
    return None

myCar1 = {
  "brand": "Ford",
  "model": "F150",
  "year": 2019
}

myCar1.setdefault("msrp", 69999)


myCar2 = defaultdict(ifNoKey)
myCar2 ["Make"] = "Ford"
myCar2 ["Model"] = "F150"
myCar2 ["Year"] = 2019
myCar2 ["msrp"] = 59999

print(myCar2["Make"])

print(myCar2["msrp"])