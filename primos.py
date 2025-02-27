#Função principal
def main():
    #Validação básica do intervalo
    while True:
        a = int(input("Digite o primeiro numero: "))
        b = int(input("Digite o segundo numero: "))

        if a < b:
            break
        else:
            print('Para um intervalo, a precisa ser menor que b\n')

    verificado = verificar_primos(a, b)
    if verificado:
        for num in verificado:
            print(num)
    else:
        print("Não foram encontrados numeros primos")

#Função de verificação
def verificar_primos(a,b):
    primos = []
    cont = 0
    #Loop para iterar sobre o intervalo
    for i in range(a, b+1):
        #Loop para verificar se é um número primo
        for j in range(i, 0, -1):
            if i % j == 0:
                cont += 1
        if cont <= 2:
            primos.append(i)
        cont = 0
    
    if len(primos) >= 1:
        return primos
    else:
        return None

main()
