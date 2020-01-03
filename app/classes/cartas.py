import random

class Cartas:
    def __init__(self):
        self.cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
        self.cartas_salvas = []

    def get_cartas(self) -> list:
        return self.cartas

    def get_cartas_salvas(self) -> list:
        return self.cartas_salvas

    def embaralhar(self) -> None:
        return random.shuffle(self.cartas)

    def retirar_carta(self) -> str:
        return self.cartas.pop(random.randint(0,len(self.cartas)-1))

    def salvar_cartas(self, carta_retirada):
        self.cartas_salvas.append(carta_retirada)

    def retornar_cartas_salvas(self) -> None:
        print(f'Cartas já viradas: {self.cartas_salvas}')



