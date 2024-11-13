import unittest
from src.ordenar_lista_ascendente import BubbleSort


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.sorter = BubbleSort()

    def tearDown(self):
        self.sorter = None

    # 1er caso de prueba - lista ordenada
    def test_lista_ordenada(self):
        self.assertEqual(self.sorter.sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    # 2do caso de prueba - lista invertida
    def test_lista_invertida(self):
        self.assertEqual(self.sorter.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # 3er caso de prueba - lista desordenada
    def test_lista_desordenada(self):
        self.assertEqual(self.sorter.sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

# if __name__ == '__main__':
#     unittest.main()
