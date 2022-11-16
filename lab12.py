# Instructions

# 1. Create a local method

# 2. Attempt to change the local() method

# 3. Print the results

def powerHouse():
    inVar = "Mitochondria"
    print(f"{inVar} is the powerhouse of the cell")

powerHouse()

locals()['inVar'] = "Something else"

powerHouse()