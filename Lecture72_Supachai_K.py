menuList = []

def showBill():
    print("--------- My Food ---------")
    totalPrice = 0
    for number in range(len(menuList)):
        totalPrice = totalPrice + menuList[number][1]
        print(menuList[number][0], menuList[number][1])
    print("Total Price = ", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName, menuPrice])

showBill()