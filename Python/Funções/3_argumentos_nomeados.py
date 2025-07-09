def salvar_carro(marca, modelo, ano, placa):
    #sala carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


#Passando argumentos NÃO NOMEADOS
#salvar_carro("Fiat", "Palio", "1990", "ABC-1234")

#Passando argumentos NOMEADOS
salvar_carro(marca="fiat", modelo="Palio", ano="1990", placa="1234")

#salvar_carro(**{"marca": "Fiat", "modelos": "Palio", "ano": "1990", "placa": "1234"})
