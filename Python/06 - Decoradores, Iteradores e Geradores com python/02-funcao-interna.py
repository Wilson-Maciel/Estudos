
def principal():
    print("Executando função principal.")

    def funcao_interna():
        print("Executando função_interna.")

    def funcao_2():
        print("Executando funcao_2.")

    funcao_interna()
    funcao_2()

principal()
