def fibonacci(check_value):
    n1 = 0
    n2 = 1
    sequence = [0, 1]
    actual_value = 0

    while actual_value < check_value:
        actual_value = n1 + n2
        sequence.append(actual_value)
        n1 = n2
        n2 = actual_value

    exists = False
    for value in sequence:
        if value == check_value:
            exists = True

    if exists:
        print("O valor informado existe na sequência de Fibonacci")
    else:
        print("O valor informado não existe na sequência de Fibonacci")


check = int(input("Qual valor deseja verificar? "))

fibonacci(check)





