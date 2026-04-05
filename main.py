class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# La clase Moto 'hereda' de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        # 'super' llama al constructor del padre (Vehiculo)
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def describir(self):
        return f"Moto: {self.marca} {self.modelo} de {self.cilindrada}cc"

# Pruebas
mi_carro = Vehiculo("Toyota", "Corolla")
mi_moto = Moto("Yamaha", "MT-07", 689)

print(mi_carro.describir())
print(mi_moto.describir())