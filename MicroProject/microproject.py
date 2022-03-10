#Take Roman Input
roman = input('Enter the Roman Letter : ')

#function for convertion
def converter(roman):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #integers corresponding to Roman Letters
    result = 0
    for i in range(len(roman)):
        #check that 1st letter's value less than its next value
        if i+1 != len(roman) and d[roman[i]] < d[roman[i+1]]:
            result = result - d[roman[i]] #if the i is lesser, then perfom subtraction
        else:
            result = result + d[roman[i]] #if the i is greater, then perfom addition
    return result

print("The Decimal number corresponding to ",roman," is : ",converter(roman))
