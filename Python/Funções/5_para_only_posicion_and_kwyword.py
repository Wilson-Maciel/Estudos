#positional only
#parâmetros somente por posição sãos os antes da barra.
#podemos passar, após a barra tanto por posição quanto nomeados.
#CONTUDO, antes da barras, passar somente por posição.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#VÁLIDO
criar_carro("Palio", "1999", "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#INVÁLIDO
criar_carro(modelo="Palio", "1999", "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#KEYWORD ONLY
#Somente poderemos passar argumentos nomeados
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano="1999", placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#KEYWORD AND POSITIONAL ONLY
#Também poderemos amarrar em um modelo hibrido.
#os primeiros argumentos são necessariamente de posição, e os argumentos após o * são, necessariamente, nomeados.
def criar_carro( modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", "1999", "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")
