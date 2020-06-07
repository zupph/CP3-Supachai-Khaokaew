menuList = []
priceList = []

def showBill():
    print("--------- My Food ---------")
    totalPrice = 0
    for number in range(len(menuList)):
        totalPrice = totalPrice + priceList[number]
        print(menuList[number], priceList[number])
    print("Total Price = ", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
