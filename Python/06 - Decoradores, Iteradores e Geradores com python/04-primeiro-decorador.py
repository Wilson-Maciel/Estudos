def meu_decorador(funcao):                      # 1. Recebe uma função como argumento
    def envelope():                             # 2. Define uma função interna (closure)
        print("Faz algo antes de executar")     #    - Pré-execução
        funcao()                                #    - Chama a função original
        print("Faz algo depois de executar")    #    - Pós-execução
    return envelope                             # 3. Retorna a função modificada


@meu_decorador
def falar():                                    #4. Função que será decorada.
    print("Ola mundo!")

falar()                                         # 5. Executa o pacote completo
#saida
#Faz algo antes de executar
#Ola mundo!
#Faz algo depois de executar
