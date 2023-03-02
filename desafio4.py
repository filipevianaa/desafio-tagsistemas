def details(data):
    total = 0
    for i in data:
        total += float(i["value"])

    for i in data:
        percentual = (float(i["value"])/total)*100
        print (f'O estado de {i["state"]} representa {percentual:,.2f}% do total de {total}')





data = [{"state": "SP", "value": "67836.43"},{"state": "RJ", "value": "36678.66"},{"state": "MG", "value": "29229.88"},{"state": "ES", "value": "27165.48"},{"state": "Outros", "value": "19849.53"}]

details(data)

