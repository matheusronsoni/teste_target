def inverte_palavra(palavra):
    palavra_invertida = ""
    for letra in range(len(palavra)-1, -1, -1):
        palavra_invertida += palavra[letra]
    
    return palavra_invertida

palavra = input("Digite uma palavra para ser invertida: ")

palavra_invertida = inverte_palavra(palavra)

print(f"A palavra invertida é: {palavra_invertida}")