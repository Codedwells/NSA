def main ():
    num1 = int(input("Please input the first value: "))
    operation = str(input("Please input the opertion sign: "))
    num2 = int(input("Please input the second value: "))

    make_calculation(num1,operation,num2)


def make_calculation(num1,operator,num2):
    answer = 0

    if operator == '+' :
            answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '/':
        answer = num1 / num2
    elif operator == '*':
        answer = num1 * num2
    else :
        print("The operator you input is not accepted!!!")
        return

    print("Your answer is: ",answer)


main()
