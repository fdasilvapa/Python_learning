lista = []

#prenche a lista
for i in range(0, 9):
    lista.append(int(input("Digite um numero: ")))

#função de ordenação
def ordenar(numeros):
    aux = 0
    for i in range(0, len(numeros) - 1):
        for i in range(0, len(numeros) - 1):
            if numeros[i] > numeros[i + 1]:
                aux = numeros[i + 1]
                numeros[i + 1] = numeros[i]
                numeros[i] = aux

    return numeros

ordenado = ordenar(lista)
for num in lista:
    print(num)
