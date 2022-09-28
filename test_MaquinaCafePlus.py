import unittest
from MaquinaCafePlus import MaquinaCafePlus
from MaquinaCafePlusException import No_coin_exception
from MaquinaCafePlusException import No_ingredientes_exception


class TestMaquinaCafe(unittest.TestCase):

    def test_insert_ingrediente(self):
        maquina = MaquinaCafePlus()
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_ingredientes("te", 1000)
        maquina.insert_ingredientes("azucar", 1000)
        maquina.insert_ingredientes("leche", 1000)
        self.assertEqual(1000, maquina.ingredientes["cafe"])
        self.assertEqual(1000, maquina.ingredientes["te"])
        self.assertEqual(1000, maquina.ingredientes["azucar"])
        self.assertEqual(1000, maquina.ingredientes["leche"])

    def test_insert_ingrediente_segunda_vez(self):
        maquina = MaquinaCafePlus()
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_ingredientes("te", 1000)
        maquina.insert_ingredientes("azucar", 1000)
        maquina.insert_ingredientes("leche", 1000)
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_ingredientes("te", 1000)
        maquina.insert_ingredientes("azucar", 1000)
        maquina.insert_ingredientes("leche", 1000)
        self.assertEqual(2000, maquina.ingredientes["cafe"])
        self.assertEqual(2000, maquina.ingredientes["te"])
        self.assertEqual(2000, maquina.ingredientes["azucar"])
        self.assertEqual(2000, maquina.ingredientes["leche"])

    def test_insert_azucar_level(self):
        maquina = MaquinaCafePlus()
        maquina.insert_azucar_nivel(5)
        self.assertEqual(maquina.azucar_nivel, 5)

    def test_insert_azucar_level_segunda_vez(self):
        maquina = MaquinaCafePlus()
        maquina.insert_azucar_nivel(5)
        maquina.insert_azucar_nivel(5)
        self.assertEqual(maquina.azucar_nivel, 10)

    def test_cafe_simple(self):
        maquina = MaquinaCafePlus()
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_coins()
        maquina.get("cafe_simple")
        self.assertEqual(maquina.ingredientes["cafe"], 1000 - 10)
        self.assertEqual(maquina.coins, 0)

    def test_cafe_simple_azucar(self):
        maquina = MaquinaCafePlus()
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_ingredientes("azucar", 1000)
        maquina.insert_azucar_nivel(5)
        maquina.insert_coins()
        maquina.get("cafe_simple")
        self.assertEqual(maquina.ingredientes["cafe"], 1000 - 10)
        self.assertEqual(maquina.ingredientes["azucar"], 1000 - 5)
        self.assertEqual(maquina.coins, 0)

    def test_capuccino(self):
        maquina = MaquinaCafePlus()
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_ingredientes("leche", 1000)
        maquina.insert_coins()
        maquina.get("capuccino")
        self.assertEqual(maquina.ingredientes["cafe"], 1000 - 10)
        self.assertEqual(maquina.ingredientes["leche"], 1000 - 200)
        self.assertEqual(maquina.coins, 0)

    def test_capucciono_azucar(self):
        maquina = MaquinaCafePlus()
        maquina.insert_ingredientes("cafe", 1000)
        maquina.insert_ingredientes("leche", 1000)
        maquina.insert_ingredientes("azucar", 1000)
        maquina.insert_azucar_nivel(5)
        maquina.insert_coins()
        maquina.get("capuccino")
        self.assertEqual(maquina.ingredientes["cafe"], 1000 - 10)
        self.assertEqual(maquina.ingredientes["leche"], 1000 - 200)
        self.assertEqual(maquina.ingredientes["azucar"], 1000 - 5)
        self.assertEqual(maquina.coins, 0)

    def test_get_cafe_simple_error_because_ingredientes(self):
        maquina = MaquinaCafePlus()
        maquina.insert_coins()
        with self.assertRaises(No_ingredientes_exception):
            maquina.get("cafe_doble")
        self.assertEqual(maquina.coins, 1)

    def test_get_error_because_monedas(self):
        maquina = MaquinaCafePlus()
        with self.assertRaises(No_coin_exception):
            maquina.get("cafe_simple")
        self.assertEqual(maquina.coins, 0)


if __name__ == '__main__':
    unittest.main()