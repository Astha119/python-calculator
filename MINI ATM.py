balance = 10000

while True:

    print("\n======MINI ATM======")
    print("1. check balance")
    print("2. debit")
    print("3. credit")
    print("4. exit")

    choice = input("enter choice :")

    if choice == "1":
        print("current balance :", balance)

    elif choice == "2":
        debit = int(input("enter debit amount :"))

        if debit <= balance:
            balance = balance-debit
            print("debit amount :", debit)
            print("remaining balance :", balance)
        else:
            print("insufficient balance")

    elif choice == "3":
        credit = int(input("enter credit amount :"))

        balance = balance + credit

        print("credited amount :", credit)
        print("updated balance :",balance)

    elif choice == "4":
        print("thank you for using mini ATM! ")
        break
    else:
        print("invalid choice")
n
