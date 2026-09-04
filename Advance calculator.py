print("=====ADVANCE CALCULATOR======")

history = []


while True:

    print("1.addition")
    print("2.subtration")
    print("3.multiplication")
    print("4.division")
    print("5.percentage")
    print("6.power")
    print("7.square root")
    print("8.factorial")
    print("9.trigonometry")
    print("10.calculation history")
    print("11.exit")

    choice = int(input("enter choice :"))

    if choice == 1:
        n = int(input("how many numbers do you want to add?"))

        total = 0

        for i in range(n):
            number = float(input("enter numbers :"))
            total = total + number
        print("Total =", total)
        item = f"Addition = {total}"
        history.append(item)


    elif choice == 2:
        n = int(input("how many numbers do you want to subtract ?"))

        total = float(input("enter first no :"))

        for i in range(n-1):
            number = float(input("enter number :"))
            total = total - number
        print("Total =",total)
        item = f"Addition = {total}"
        history.append(item)

    elif choice == 3:
        n = int(input("how many numbers do you want to multiply ?"))

        total = 1

        for i in range(n):
            number = float(input("enter number :"))
            total = total*number
        print("Total :", total)
        item = f"Addiition = {total}"
        history.append(item)

    elif choice == 4:
        n = int(input("how many numbers do you want to divide ?"))

        total = float(input("enter first number :"))

        for i in range(n-1):
            number = float(input("enter number :"))
            if number == 0:
                print("invalid")
            else:
                total = total / number
        print("Total :", total)
        item = f"Addition = {total}"
        history.append(item)


    elif choice == 5:
        obtained = float(input("enter obtained value:"))
        total = float(input("enter total value:"))
        percentage = (obtained / total) * 100
        print("percentage =", percentage, "%")
        item = f"Addition = {total}"
        history.append(item)


    elif choice == 6:
        number = float(input("enter number :"))
        power = float(input("input power :"))
        ans = number ** power
        print("power =", ans)
        item = f"Addition = {total}"
        history.append(item)

    elif choice == 7:
        import math
        number = float(input("enter a number :"))
       
        result = math.sqrt(number)
        print("squareroot =", result)
        item = f"Addition = {total}"
        history.append(item)

    elif choice == 8:
        n = int(input("enter number :"))
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        print("factorial =", fact)
        item = f"Addition = {total}"
        history.append(item)

    elif choice == 9:
        import math
        choice = input("enter sin/ cos/ tan/ cosec/ cot/ sec :" )
        angle = float(input("enter angle in degree :"))
        radian = math.radians(angle)

        if choice == "sin":
            result = math.sin(radian)
            print("sin",round(result, 2) )

        elif choice == "cos":
              result = math.cos(radian)
              print("cos",round(result, 2))

        elif choice == "tan":
            result = math.tan(radian)
            print("tan", round(result, 2))

        elif choice == "cot":
            result = 1/math.tan(radian)
            print("cot", round(result, 2))

        elif choice == "cosec":
            result = 1/math.sin(radian)
            print("cosec", round(result, 2))

        elif choice == "sec":
            result = 1/math.cos(radian)
            print("sec", round(result, 2))
            item = f"Addition = {total}"
            history.append(item)

    elif choice == 10:
        if history:
            for item in history:
                print(item)
        else:
            print("no calculation history")

    elif choice == 11:
        print("thank you for using calculator")
        break
