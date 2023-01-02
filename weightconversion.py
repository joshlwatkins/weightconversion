#Program that ask for the weight in pounds or kilos and converts it to the opposite weight

unit = input('(L)bs or (K)g: ')
weight = int(input('Weight: '))

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")
