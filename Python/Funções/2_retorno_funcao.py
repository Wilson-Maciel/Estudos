def calcular_total(numeros):
    return sum(numeros)

#retorna 2 argumentos
def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


#caso não passe o retorno da funçao. A saída em um print terá o retur=none
def func_3():
    print("Olá Mundo!")




print(calcular_total([10,20,34]))

print(retorna_antecessor_sucessor(10))

print(func_3())#return=none
