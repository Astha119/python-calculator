a = float(input("Enter first number :"))
op = input("Enter operator(+, -, *, /) :")
b = float(input("Enter second number:"))

if op == "+":
    print("result = ", a + b)

elif op == "-":
    print("result =",a-b)

elif op == "*":
    print("result =",a*b)

elif op == "/":
    if b!= 0:
       print("result = ",a/b)
    else:
        print("cannot divide by zero")

else:
    print("invalid operator")

    