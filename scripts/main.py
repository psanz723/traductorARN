import Diccionario
import TraductorConstantes
from SecuenciaARN import SecuenciaAminoacido

# Programa principal
def main():

    # 1. Leer secuencia ARN desde archivo
    ruta_entrada = "datos-raw/secuenciaARN.txt"
    with open(ruta_entrada, "r") as f:
        secuencia = f.read().strip()

    print("Secuencia ARN cargada:", secuencia)

    # 2. Crear objeto de traducción
    obj = SecuenciaAminoacido(secuencia)

    # 3. Validar secuencia
    try:
        obj.validar()
        print("Validación correcta.")
    except ValueError as e:
        print("ERROR:", e)
        return

    # 4. Traducir ARN → aminoácidos (1 letra)
    obj.traduceARNtoAminoacido()
    print("Aminoácidos (1 letra):", obj.st_secuenciaAminoacido)

    # 5. Convertir a formato 3 letras
    obj.convertir_a_3_letras()
    print("Aminoácidos (3 letras):", obj.st_secuenciaAminoacido)

    # 6. Guardar salida en resultados
    ruta_salida = "resultados/salida_3_letras.txt"
    with open(ruta_salida, "w") as f:
        f.write(obj.st_secuenciaAminoacido)

    print("Salida guardada en:", ruta_salida)


if __name__ == "__main__":
    main()
 # 7. Registrar runlog
    import datetime
    ruta_runlog = "resultados/runlog.txt"

    with open(ruta_runlog, "a") as log:
        log.write("\n==============================\n")
        log.write(f"Fecha y hora: {datetime.datetime.now()}\n")
        log.write(f"Secuencia ARN: {secuencia}\n")
        log.write(f"Aminoácidos (1 letra): {obj.st_secuenciaAminoacido}\n")
        log.write(f"Aminoácidos (3 letras): {obj.st_secuenciaAminoacido}\n")
        log.write(f"Salida guardada en: {ruta_salida}\n")
        log.write("==============================\n")