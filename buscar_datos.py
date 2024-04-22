import unittest
def buscar_datos(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key", key, "value", value)
        for k, v in value.items():
            print("k", k, "v", v)

database = {
    "persona1": {
        "primer_nombre": "Lucas",
        "segundo_nombre": "Alejandro",
        "primer_apellido": "Boschin",
        "segundo_apellido": "Antonioni"
    }
}
resultado= buscar_datos("Lucas", "Alejandro", "Boschin", "Antonioni", **database)

database = {
    "persona2": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Andrés",
        "primer_apellido": "Messi",
        "segundo_apellido": "Cuccittini"
    }
}
resultado= buscar_datos("Lionel", "Andrés", "Messi", "Cuccittini", **database)

database = {
    "persona3": {
        "primer_nombre": "Marcelo",
        "segundo_nombre": "Daniel",
        "primer_apellido": "Gallardo"
    }
}
resultado= buscar_datos("Marcelo", "Daniel", "Gallardo", **database)

database = {
    "persona4": {
        "primer_nombre": "Diego",
        "segundo_nombre": "Armando",
        "primer_apellido": "Maradona"
    }
}
resultado= buscar_datos("Diego", "Armando", "Maradona", **database)

database = {
    "persona5": {
        "primer_nombre": "Cristiano",
        "segundo_nombre": "Ronaldo",
        "primer_apellido": "dos Santos",
        "segundo_apellido": "Aveiro"
    }
}
resultado= buscar_datos("Cristiano", "Ronaldo", "dos Santos", "Aveiro", **database)

class test_buscar_datos(unittest.TestCase):
    def test_buscar_datos_persona1(self):
        resultado = buscar_datos("Lucas", "Alejandro", "Boschin", "Antonioni", **database)
        self.assertEqual(resultado, "persona1", True)

    def test_buscar_datos_persona2(self):
        resultado = buscar_datos ("Lionel", "Andrés", "Messi", "Cuccittini", **database)    
        self.assertEqual(resultado, "persona2", True)

    def test_buscar_datos_persona3(self):
        resultado = buscar_datos("Marcelo", "Daniel", "Gallardo", **database)
        self.assertEqual(resultado, "persona3", True)

    def test_buscar_datos_persona4(self):
        resultado = buscar_datos("Diego", "Armando", "Maradona", **database)
        self.assertEqual(resultado, "persona4", True)

    def test_buscar_datos_persona5(self):
        resultado = buscar_datos("Cristiano", "Ronaldo", "dos Santos", "Aveiro", **database)
        self.assertEqual(resultado, "persona5", True)

    def test_buscar_datos_persona6(self):
        resultado = buscar_datos("Kylian", "Mbappé", "Lottin", **database)
        self.assertEqual(resultado, "persona6", False) 

    unittest.main()



        

