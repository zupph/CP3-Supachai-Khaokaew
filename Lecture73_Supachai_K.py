systemMenu = {"ข้าวไข่เจียว": 40, "ข้าวไข่ต้ม": 30, "ข้าวไข่ตุ๋น": 50, "ข้าวไข่สตาร์": 35}
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
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()
