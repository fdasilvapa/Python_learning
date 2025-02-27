num = int(input("Digite um numero: "))

def fibonacci(numero):
    soma = 1
    lista = [1]
    for i in range(1, numero - 1):
        lista.append(soma)
        soma = lista[i - 1] + lista[i]
    
    for num in lista:
        print(num)
    print(soma)

fibonacci(num)
