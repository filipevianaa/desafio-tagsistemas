import json  

f = open('dados.json')

data = json.load(f)

def find_max():
    max = 0
    for i in data:
        if i["valor"] > max:
            max = i["valor"]
    return max

def find_min():
    min = 999999999999999
    for i in data:
        if i["valor"] <= min and i["valor"] != 0:
            min = i["valor"]
    return min

def calc_average():
    count_days = 0
    sum = 0
    for i in data:
        if i["valor"] != 0:
            sum += i["valor"]
            count_days += 1
    average = sum/count_days
    return average

print(f"O menor valor de faturamento foi de: {find_min()}")
print(f"O maior valor de faturamento foi de: {find_max()}")
print(f"A média de faturamento no mês foi de: {calc_average()}" )


f.close()

