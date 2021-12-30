<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>

    Considere el siguiente problema:

    Escriba un programa corto de una sola línea permita filtrar todos los elementos de una array sin posibles repeticiones.
    
     N = 4 
    
         [7, 7, 7, 8]

     Resultado
	 
         [7,8]


    Observe el orden del elemento repetido. Éste debe de estar en el orden correcto.
    Atienda a números, letras y palabras.
    
    El resultado debe ser un array con los elementos no repetidos.
    
    
    Se atiente al siguiente ejemplo:
   
    N = 1          N = 2          N = 3          N = 4               N = 5
      
        [6]        [6, 6]         [6, 6, 9]      [6, 6, 9, 'a']      [6, 6, 9, 'a', 'a']        
                 
    Resultado:
 
	    [6]	       [6]	      [6, 9]         [6, 9, 'a']         [6, 9, 'a']      
                                  
    
    En la carpeta 'src\kata.py' se encuentra el fichero con la definición de nuestro método vacío.
    En la carpeta 'tests\test_kata.py' se encuentra el fichero con la suite de test.
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.
    
    A continuación se muestran los resultado que se tienen que obtener tras desarrollar el algoritmo.

    [Test suite]

    def test_apply_01(self)
    def test_apply_02(self)
    def test_apply_03(self)
    def test_apply_04(self)
    def test_apply_05(self)
    def test_apply_06(self)
    def test_apply_07(self)
    def test_apply_08(self)
    def test_apply_09(self)
    def test_apply_10(self)
    def test_apply_11(self)
    def test_apply_12(self)
    def test_apply_13Null(self)

    Tests run: 

    tests/test_kata.py::Test_kata::test_apply_01 PASSED                      [  7%]
    tests/test_kata.py::Test_kata::test_apply_02 PASSED                      [ 15%]
    tests/test_kata.py::Test_kata::test_apply_03 PASSED                      [ 23%]
    tests/test_kata.py::Test_kata::test_apply_04 PASSED                      [ 30%]
    tests/test_kata.py::Test_kata::test_apply_05 PASSED                      [ 38%]
    tests/test_kata.py::Test_kata::test_apply_06 PASSED                      [ 46%]
    tests/test_kata.py::Test_kata::test_apply_07 PASSED                      [ 53%]
    tests/test_kata.py::Test_kata::test_apply_08 PASSED                      [ 61%]
    tests/test_kata.py::Test_kata::test_apply_09 PASSED                      [ 69%]
    tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [ 76%]
    tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 84%]
    tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 92%]
    tests/test_kata.py::Test_kata::test_apply_13Null PASSED                  [100%]



## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
