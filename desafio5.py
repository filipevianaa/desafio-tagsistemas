def invert(string):
    new_string = ""
    for index in range(len(string), 0, -1):
        new_string += string[index-1]

    return new_string

str = input("Digite o texto que deseja inverter ")
print(invert(str))