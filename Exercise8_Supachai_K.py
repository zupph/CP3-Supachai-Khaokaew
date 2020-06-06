usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == "inmad" and passwordInput == "1234":
    moonPrice = 20
    venusPrice = 120
    marsPrice = 70
    mercuryPrice = 50
    sunPrice = 7000
    jupiterPrice = 1400
    saturnPrice = 1200
    uranusPrice = 500
    print("        Welcome to my shop")
    print("        ------------------")
    print("           price list")
    print("no. product                       price")
    print("------------------------------------------")
    print("1. earth's moon                  " + str(moonPrice) + " THB")
    print("2. venus                         " + str(venusPrice) + " THB")
    print("3. mars                          " + str(marsPrice) + " THB")
    print("4. mercury                       " + str(mercuryPrice) + " THB")
    print("5. sun                           " + str(sunPrice) + " THB")
    print("6. jupiter                       " + str(jupiterPrice) + " THB")
    print("7. saturn                        " + str(saturnPrice) + " THB")
    print("8. uranus                        " + str(uranusPrice) + " THB")
    print("------------------------------------------")
    productInput = int(input("What do you want ? (please enter product no.) : "))
    if productInput < 1 or productInput > 8:
        print("We don't have product that you want, please go to other shop !!!!")
    else:
        quantityInput = int(input("How many ? "))
        if productInput == 1:
            productName = "earth's moon"
            totalPrice = moonPrice * quantityInput
        elif productInput == 2:
            productName = "venus"
            totalPrice = venusPrice * quantityInput
        elif productInput == 3:
            productName = "mars"
            totalPrice = marsPrice * quantityInput
        elif productInput == 4:
            productName = "mercury"
            totalPrice = mercuryPrice * quantityInput
        elif productInput == 5:
            productName = "sun"
            totalPrice = sunPrice * quantityInput
        elif productInput == 6:
            productName = "jupiter"
            totalPrice = jupiterPrice * quantityInput
        elif productInput == 7:
            productName = "saturn"
            totalPrice = saturnPrice * quantityInput
        else:
            productName = "uranus"
            totalPrice = uranusPrice * quantityInput


        if quantityInput > 1:
            word = " But we have one " + productName + " in the sky, you can not order it more than one."
            if productName == "venus" or productName == "mars" or productName == "uranus":
                s = "es"
            elif productName == "mercury":
                productName = "mercurie"
                s = "s"
            else:
                s = "s"
        elif quantityInput == 1:
            s = ""
            word = ""

        if quantityInput < 1:
            print("Don’t be annoying, go outside!!!!")
        else:
            print("Total price of " + str(quantityInput) + " " + productName + s + " is " + str(totalPrice) + " THB." + word)
            print("Thank you.")
else:
    print("Sorry!, you must learn borntodev's Complete Python3 Programming in section 1 - 6 before you login again !!!!!")
