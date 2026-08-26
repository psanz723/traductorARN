import TraductorConstantes         # Constantes a utilizar en el programa
import Diccionario                 # Diccionario con la traducción ARN-AA

# Clase para definir una secuencia ARN.
# Es una clase padre
class SecuenciaARN:

    # Atributos de clase. Son compartidos por todos los objetos
    _NUM_AA_SEC_ARN=TraductorConstantes.NUM_SIMBOLO_ARN_AMINOACIDO       # Número de AA en la secuencia ARN
    
    def __init__ (self, st_secuenciaARN):
        self._st_secuenciaARN = st_secuenciaARN

    @property                                                    # getter NUM_AA_SEC_ARN
    def NUM_AA_SEC_ARN (self):
        return self._NUM_AA_SEC_ARN
    
    @property                                                          # getter _st_secuenciaARN
    def st_secuenciaARN (self):
        return self._st_secuenciaARN

    @st_secuenciaARN.setter                                            # setter _st_secuenciaARN
    def st_secuenciaARN (self, st_secuenciaARN):
        self._st_secuenciaARN = st_secuenciaARN
    
    def print_info (self):
        print (f"SecuenciaARN:{self.st_secuenciaARN}")

# Clase para definir una secuencia ARN.
# Es una clase hija
class SecuenciaAminoacido (SecuenciaARN):
    def __init__ (self, st_secuenciaARN):
        super().__init__(st_secuenciaARN)
        self._st_secuenciaAminoacido = "No traducida"                  # Se inicializa a un valor por defecto.

    @property                                                          # getter _st_secuenciaAminoacido
    def st_secuenciaAminoacido (self):
        return self._st_secuenciaAminoacido

    @st_secuenciaAminoacido.setter                                     # setter _st_secuenciaAminoacido
    def st_secuenciaAminoacido (self, st_secuenciaAminoacido):
        self._st_secuenciaAminoacido = st_secuenciaAminoacido

    # Traduce una secuencia ARN en aminoacidos y lo almacena en el atributo de instancia _st_secuenciaAminoacido
    def traduceARNtoAminoacido (self):
        st_aminoacido = ""                # String para almacenar la traducción concactenada de AA
        for i in range (0, len(self.st_secuenciaARN), 3):
            #print ("\t\t\t\t" + self.st_secuenciaARN[i:i+3] + " -> " + Diccionario.dic_codigo_genetico.get(self.st_secuenciaARN[i:i+3], "X"))
            st_aminoacido = st_aminoacido + Diccionario.dic_codigo_genetico.get(self.st_secuenciaARN[i:i+3], "X")
        self.st_secuenciaAminoacido = st_aminoacido
    
    def print_info (self):
        super().print_info()
        print (f"Secuencia aminoacidos:{self.st_secuenciaAminoacido}")