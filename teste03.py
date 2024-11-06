import json

def calculo_faturamento(info_faturamento):
    faturamentos = [dia["faturamento"] for dia in info_faturamento if dia["faturamento"] > 0]
    
    menor_faturamento = min(faturamentos)
    
    maior_faturamento = max(faturamentos)
    
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, media_mensal, dias_acima_da_media

with open("faturamento.json") as arquivo:
    info_faturamento = json.load(arquivo)
    
menor_faturamento, maior_faturamento, media_mensal, dias_acima_da_media = calculo_faturamento(info_faturamento)

print(f"O menor faturamento foi de R${menor_faturamento}")
print(f"O maior faturamento foi de R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
    
    
        