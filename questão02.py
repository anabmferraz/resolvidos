# Questão 02 - Sequência Fibonacci

def verifica_fibonacci(numero):
    a, b = 0, 1

    if numero == 0 or numero == 1:
        return True

    while b < numero:
        a, b = b, a + b
        if b == numero:
            return True
    
    return False


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
