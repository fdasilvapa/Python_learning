import string

def separar_palavras(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto.split()

    return palavras

def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    return contagem

def main():
    texto = input("Digite uma frase: ")
    separado = separar_palavras(texto)
    print(f'Contagem: {contar_palavras(separado)}')

main()
