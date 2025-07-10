def meu_decorador(funcao):                      # 1. Recebe uma função como argumento
    def envelope(*args, **kwargs):              # 2. Define uma função interna (closure)
        print("Faz algo antes de executar")     #    - Pré-execução
        resultado = funcao(*args, **kwargs)     #    - Chama a função original
        print("Faz algo depois de executar")
        return resultado                        #    - Pós-execução
    return envelope                             # 3. Retorna a função modificada


@meu_decorador
def falar(nome, outro_argumento):                                    #4. Função que será decorada.
    print(f"Ola mundo! {nome}")
    return nome.upper()


resultado = falar("Wilson", 1000)
print(resultado)
# 5. Executa o pacote completo
#saida
#Faz algo antes de executar
#Ola mundo!
#Faz algo depois de executar
