from itertools import tee
from math import prod
from this import d
from MaquinaCafePlusException import No_coin_exception
from MaquinaCafePlusException import No_ingredientes_exception


class MaquinaCafePlus():

    def __init__(self):
        self.ingredientes = {
            "cafe": 0,
            "azucar": 0,
            "te": 0,
            "leche": 0,
        }

        self.recetas = {
            "cafe_simple": {
                "cafe": 10,
            },
            "cafe_doble": {
                "cafe": 20,
            },
            "te_simple": {
                "te": 10,
            },
            "capuccino": {
                "cafe": 10,
                "leche": 200,
            }
        }
        self.azucar_nivel = 0
        self.coins = 0

    def insert_ingredientes(self, tipo, cantidad):
        self.ingredientes[str(tipo)] += cantidad

    def insert_coins(self):
        self.coins += 1

    def insert_azucar_nivel(self, azucar):
        self.azucar_nivel += azucar

    def get(self, receta):
        if self.coins < 1:
            raise No_coin_exception
        producto = self.recetas[receta]
        for ingrediente in producto.keys():
            if ingrediente != "azucar":
                if self.coins < 1:
                    raise No_coin_exception
                if self.ingredientes[ingrediente] < producto[ingrediente]:
                    raise No_ingredientes_exception

        for ingrediente in producto:
            self.ingredientes[ingrediente] -= producto[ingrediente]

        self.ingredientes["azucar"] -= self.azucar_nivel
        self.coins -= 1