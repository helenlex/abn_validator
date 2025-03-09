#abn = input('Please input an ABN without spaces:')
abn = str(51824753556)
#Subtract 1 from the first (left-most) digit of the ABN to give a new 11 digit number
newabn = (str(int(abn[0]) - 1)) + abn[1:]

#Multiply each of the digits in this new number by a "weighting factor" based on its position as shown in the table below

weighting_factor = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

## setting up the index so it can auto-increment
i = 0

## declaring variable "sum"
sum = 0

for digit in newabn:
    result = int(digit) * weighting_factor[i]
    i += 1
    sum += result
    

