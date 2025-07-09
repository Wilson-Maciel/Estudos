def mensagem(nome):
    print(f"Executando mensagem")
    return print(f"Oi {nome}")


def mensagem_longa(nome):
    print(f"Executando mensagem_longa")
    return f"Olá tudo bem com você {nome}"

def executar(funcao, nome):
    print(f"Executando Executar")
    return funcao(nome)


executar(mensagem, 'wilson')
print(executar(mensagem, 'Wilson'))
