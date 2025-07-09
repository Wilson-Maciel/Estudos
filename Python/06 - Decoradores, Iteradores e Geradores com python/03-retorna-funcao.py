def calculadora(operacao):
    def soma(a, b):
        return a + b #retorna a operaçao.

    def sub(a, b):
        return a - b #retorna a operaçao.

    match operacao:      # Match/Case para seleção
        case "+":
            return soma  # Retorna a função soma
        case "-":
            return sub   # Retorna a função subtração

# chamando o retorno da função somar:
#retornar a função 'somar' e guardar em uma variável "somar".
somar = calculadora("+")
#chamar a variável somar, que é a função 'soma como retorno da função calculadora
print(f"2 + 3 = {somar(2, 3)}")
# Saída: 5
