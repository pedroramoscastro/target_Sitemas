# Define a função is_fib_number para avaliar se o número informado pelo usuário pertence à sequência de Fibonacci
def is_fib_number(num):
    # Define os valores iniciais da sequência
    a = 0
    b = 1
    # Enquanto o valor b (que é a soma dos valores da sequência) for menor que o número informado pelo usuário, a soma segue sendo feita
    while b<num:
        c = a+b
        a = b
        b = c
        # No momento em que um dos valores incrementados é igual ao valor informado pelo usuário, então a execução da função é interrompida e o valor retornado é true
    if b==num or a==num:
        return True
        # Caso nenhum dos valores incrementados seja igual a num e a variável de maior valor seja maior que num, então a execução da função é interrompida e o valor retornado é false        
    if b > num:
        return False
# Solicita um valor ao usuário e o converte para o tipo inteiro
num =int(input("Informe um número para saber se ele pertence à sequência de Fibonacci: \n"))

# Se o valor retornado pela função for true, então o número pertence à sequência
if is_fib_number(num):
    print(f"{num} é um número de Fibonacci.")
    
# Se o valor retornado pela função for false, então o número NÃO pertence à sequência    
else:
    print(f"{num} NÃO é um número de Fibonacci.")