import _engine.operations as op
import _engine.program as p

program_active = True
operation = 0
result = 0
while program_active:
    try:
        num_1 = input("Enter your first number: ")
        if num_1.lower() == 'x': 
            program_active = False
            continue
        else:
            num_1 = float(num_1)

        num_2 = input("Enter your second number: ")
        if num_2.lower() == 'x': 
            program_active = False
            continue
        else:
            num_2 = float(num_2)      
        
    except:
        print("Please enter a valide input. The input has to be a number")
        continue

    print("Choose one of the operations to be performed on the numbers you have entered:")
    print("1 - Add both numbers")
    print("2 - Substract both numbers")
    print("3 - Multiply both numbers")
    print("4 - Divide both numbers")
    print("x - Exit the program")
    operation = input("Enter your choice: ")

    if operation.lower() == 'x':
        program_active = False
        continue
    else:
        try:
            operation = int(operation)
        except:
            print("Please enter a valid input between 0 and 4 both")
            continue
        match operation:
            case 1:
                print("Adding...")
                result = op.add(num_1, num_2)
            case 2:
                print("Substracting...")
                result = op.substract(num_1, num_2)
            case 3:
                print("Multiplying...")
                result = op.multiply(num_1, num_2)
            case 4:
                print("Diviting...")
                result = op.divide(num_1, num_2)
            case _ if operation < 0 or operation > 4:
                print("Please enter a valid input between 0 and 4 both inclusive or 'X' to exit")

        print(result)


