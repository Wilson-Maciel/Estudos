def criar_carro( modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", "1999", "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")
