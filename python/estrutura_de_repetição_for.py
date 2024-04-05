texto = input("Escreva um texto aqui: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ") #Se tirar o end = ele fica pulando linha a cada execução.
print( )


for numero in range(0, 16, 1):
    print(numero, end=" ")

