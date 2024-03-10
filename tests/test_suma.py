# LLibreria pytest per a executar tests
import pytest

# Importar arxiu de l'exercici
from exercicis.operacions import suma

# Classe per a la creació de tests.
class TestClass:

    # Test per a l'operació suma
    def testSuma(self):
        assert suma(3,1) == 4
        assert suma(-3,-2) == -5
        assert suma(-9,6) == -3
        assert suma(7,-4) == 3
