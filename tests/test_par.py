# LLibreria pytest per a executar tests
import pytest

# Importar arxiu de l'exercici
from exercicis.operacions import esParell

# Classe per a la creació de tests.
class TestClass:

    # Test per a l'operació esParell
    def test_par(self):
        assert esParell(4) == "parell"
        assert esParell(5) == "imparell"
        assert esParell(6) == "parell"
        assert esParell(1) == "imparell"
