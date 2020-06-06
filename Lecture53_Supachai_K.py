def vatCalculate(totalPrice):
    result = totalPrice * 1.07
    return result
totalPrice = int(input("enter total price : "))
print(vatCalculate(totalPrice))
