def powerHouse():
    inVar = "Mitochondria"
    print(f"{inVar} is the powerhouse of the cell")

powerHouse()

locals()['inVar'] = "Something else"

powerHouse()