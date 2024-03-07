#Questão 03 - Faturamento diário de uma Distribuidora

import json

with open('dados.json') as json_file:
    dados = json.load(json_file)

faturamentos = [dia['valor'] for dia in dados]
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

print("Menor valor de faturamento:", menor_faturamento)
print("Maior valor de faturamento:", maior_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)