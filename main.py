import _engine.operations as op


operation = 0
result = 0

while True:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except:
        print("Please enter a valide input. The input has to be a number")
        continue
    break

while True:
    print("Choose one of the operations to be performed on the numbers you have entered:")
    print("1 - Add both numbers")
    print("2 - Substract both numbers")
    print("3 - Multiply both numbers")
    print("4 - Divide both numbers")
    print("0 - Exit the program")

    operation = int(input("Enter your choice: "))

    


    match operation:
        case 1:
            result = op.add(num1, num2)
        case 2:
            result = op.substract(num1, num2)
        case 3:
            result = op.multiply(num1, num2)
        case 4:
            result = op.divide(num1, num2)
        case 0:
            exit()
        case _ if operation < 0 or operation > 4:
            print("Please enter a valid input between 0 and 4 both  inclusive")

    print(result)
            


    
    



# while True:
#     try:
#         num1 = float(input("Enter your first number: "))
#     except:
#         print("Please enter a valide input. The input has to be a number")
#         continue

#     try:
#             num1 = float(input("Enter your first number: "))
#     except:
#         print("Please enter a valide input. The input has to be a number")
#         continue

#     break


# print(op.add(4.4,5))
# print(op.substract(10.2, 5))
# print(op.multiply(2,3.3))
# print(op.divide(10,5.5))