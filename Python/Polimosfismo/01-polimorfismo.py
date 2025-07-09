
#Definindo a classe pai
class Passaro:
    def voar(self):
        print("Voando...")


class pardal(Passaro):
    def voar(self):
        #aqui utilizaremos o método voar da
        #classe pai sem adicionar nenhum comprotamento diferente
        super().voar()

class avestruz(Passaro):
    def voar(self):
        #aqui daremo um comportamento diferente para o método voar.
        print('Avestruz não pode voar.')

# FIXME: exemplo ruim do uso de herança para ganhar o método voar.
class aviao(Passaro):
    def voar(self):
        #aqui daremos um comportamento diferente para o métod voar.
        print('Avião está decolando')

#aqui temos o polimorfismo.
#o mesmo método voar() assumirá comprotamentos diferentes de acordo
#com o que foi implementado.
#o método possui um comportamento padrão, contudo podemos alterá-lo.

def plano_voo(obj):
    obj.voar()


plano_voo(pardal())

plano_voo(avestruz())

plano_voo(aviao())
