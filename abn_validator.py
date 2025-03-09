#abn = input('Please input an ABN without spaces:')
abn = str(51824753556)
#Subtract 1 from the first (left-most) digit of the ABN to give a new 11 digit number
newabn =(str(int(abn[0]) - 1)) + abn[1:]
print(newabn)