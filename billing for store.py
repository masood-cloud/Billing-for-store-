item = 0
while True:
    userInput = str(input("Enter the price: \n"))
    if userInput != 'q':
        item = item + int(userInput)
        print(f"total oder so far so far {item}")


    else:
        print("Thank you for shopping")
        print(f"Your total bill is {item}")
        break
