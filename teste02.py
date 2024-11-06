def contagem_fibonacci(num):
    a , b = 0 , 1
    if num == a or num == b:
        return f"O número {num} pertence a sequência de Fibonacci"
    
    while b < num: 
        a , b = b , a + b
    
    if b == num:
        return f"O número {num} pertence a sequência de Fibonacci"
    else: 
        return f"O número {num} não pertence a sequência de Fibonacci"

numero = int(input("Digite um número para verificarmos se pertence ou a sequência de Fibonacci: ")) 
print(contagem_fibonacci(numero))