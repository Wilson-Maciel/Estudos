
#criar a classe celular
class Celular:
    #inicie a classe celular com as configurações padrão
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100
    #crie método para descarregar 10%
    #da bateria até o mínimo de 10%,
    # mande recarregar quando for = 10%
    def descarregar(self):
        if self.bateria > 10:
            self.bateria -= 10
            return f"Bateria descarregando. Agora está em {self.bateria}%"
        elif self.bateria == 10:
            self.bateria -= 1
            return f"A bateria está em 9%, recarregue!"
        else:
            return f"Bateria abaixo de 10%! Recarregue!"
    def recarregar(self):
        self.bateria = 100
        return f"Bateria RECARREGADA: Agora está em {self.bateria}%"

#crie dois objetos(intâncias) diferentes:

iphone = Celular('Apple', 'iphone 15')

galaxy = Celular('Samsung', 'Galaxy s26 ultra')

#teste o método descarregar


print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.descarregar())
print(galaxy.bateria)
print(galaxy.recarregar())
print(galaxy.bateria)
