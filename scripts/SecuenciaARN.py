import TraductorConstantes         # Constantes a utilizar en el programa
import Diccionario                 # Diccionario con la traducción ARN-AA

# Clase para definir una secuencia ARN.
# Es una clase padre
class SecuenciaARN:

    # Atributos de clase. Son compartidos por todos los objetos
    _NUM_AA_SEC_ARN = TraductorConstantes.NUM_SIMBOLO_ARN_AMINOACIDO       # Número de AA en la secuencia ARN
    
    def __init__(self, st_secuenciaARN):
        self._st_secuenciaARN = st_secuenciaARN

    @property                                                    # getter NUM_AA_SEC_ARN
    def NUM_AA_SEC_ARN(self):
        return self._NUM_AA_SEC_ARN
    
    @property                                                          # getter _st_secuenciaARN
    def st_secuenciaARN(self):
        return self._st_secuenciaARN
import TraductorConstantes         # Constantes a utilizar en el programa
import Diccionario                 # Diccionario con la traducción ARN-AA

# Clase para definir una secuencia ARN.
# Es una clase padre
class SecuenciaARN:

    # Atributos de clase. Son compartidos por todos los objetos
    _NUM_AA_SEC_ARN = TraductorConstantes.NUM_SIMBOLO_ARN_AMINOACIDO       # Número de AA en la secuencia ARN
    
    def __init__(self, st_secuenciaARN):
        self._st_secuenciaARN = st_secuenciaARN

    @property                                                    # getter NUM_AA_SEC_ARN
    def NUM_AA_SEC_ARN(self):
        return self._NUM_AA_SEC_ARN
    
    @property                                                          # getter _st_secuenciaARN
    def st_secuenciaARN(self):
        return self._st_secuenciaARN

    @st_secuenciaARN.setter                                            # setter _st_secuenciaARN
    def st_secuenciaARN(self, st_secuenciaARN):
        self._st_secuenciaARN = st_secuenciaARN
    
    def print_info(self):
        print(f"SecuenciaARN:{self.st_secuenciaARN}")

    # MÉTODO AÑADIDO (NECESARIO PARA main.py)
    def codones(self):
        sec = self.st_secuenciaARN
        lista_codones = []
        for i in range(0, len(sec), 3):
            codon = sec[i:i+3]
            if len(codon) == 3:
                lista_codones.append(codon)
        return lista_codones

    # MÉTODO NUEVO: Validación de la secuencia ARN
    def validar(self):
        """
        Valida la secuencia ARN antes de traducirla.
        - Solo permite A, U, C, G
        - Longitud múltiplo de 3
        - No vacía
        """
        sec = self.st_secuenciaARN

        if not sec:
            raise ValueError("La secuencia ARN está vacía.")

        bases_validas = {"A", "U", "C", "G"}
        for base in sec:
            if base not in bases_validas:
                raise ValueError(f"Base no válida encontrada: {base}")

        if len(sec) % 3 != 0:
            raise ValueError("La longitud de la secuencia no es múltiplo de 3.")


# Clase para definir una secuencia ARN.
# Es una clase hija
class SecuenciaAminoacido(SecuenciaARN):
    def __init__(self, st_secuenciaARN):
        super().__init__(st_secuenciaARN)
        self._st_secuenciaAminoacido = "No traducida"                  # Se inicializa a un valor por defecto.

    @property                                                          # getter _st_secuenciaAminoacido
    def st_secuenciaAminoacido(self):
        return self._st_secuenciaAminoacido

    @st_secuenciaAminoacido.setter                                     # setter _st_secuenciaAminoacido
    def st_secuenciaAminoacido(self, st_secuenciaAminoacido):
        self._st_secuenciaAminoacido = st_secuenciaAminoacido

    # Traduce una secuencia ARN en aminoacidos y lo almacena en el atributo de instancia _st_secuenciaAminoacido
    def traduceARNtoAminoacido(self):
        # Validación antes de traducir
        self.validar()

        st_aminoacido = ""                # String para almacenar la traducción concatenada de AA
        for i in range(0, len(self.st_secuenciaARN), 3):
            st_aminoacido = st_aminoacido + Diccionario.dic_codigo_genetico.get(self.st_secuenciaARN[i:i+3], "X")
        self.st_secuenciaAminoacido = st_aminoacido
    
    def print_info(self):
        super().print_info()
        print(f"Secuencia aminoacidos:{self.st_secuenciaAminoacido}")