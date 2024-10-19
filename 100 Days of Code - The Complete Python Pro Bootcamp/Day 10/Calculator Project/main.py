def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply (n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    continue_processing = True


    first_num = input("First number: ")
    while continue_processing:
        operator = input("Operator: ")
        second_num = input("Second number: ")

        result = operations[operator](float(first_num),float(second_num))
        print(result)
        answer = input("Loops result as first number?: ")
        if answer == "yes":
            first_num = result
        else:
            continue_processing = False
            calculator()

calculator()




