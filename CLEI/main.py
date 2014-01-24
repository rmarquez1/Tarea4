from CLEI.apps.clei.clei import Clei
import sys
import unittest

class CleiTester(unittest.TestCase):
# Test de listar los paises participantes en la conferencia
    def testPaisConferencia(self):
        clei = CLEI(3)
        clei.crear_articulos()
        
        clei.set_aceptables(1,4.5)
        clei.set_aceptables(2,4)
        clei.set_aceptables(3,3)
        clei.set_aceptables(4,5)
        clei.set_aceptables(5,4.5)
        clei.set_aceptables(6,4.5)
        
        
        lista_paises = clei.paises_conferencia()
        self.assertEquals('Venezuela', lista_paises[0])
        
if __name__ == '__main__':
    unittest.main()