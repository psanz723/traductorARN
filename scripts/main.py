import Diccionario
import TraductorConstantes
from SecuenciaARN import SecuenciaAminoacido
import datetime
import csv

def main():

    print("=== Traductor ARN → Aminoácidos ===")

    # 1. Leer secuencia ARN desde archivo
    ruta_entrada = "datos-raw/secuenciaARN.txt"
    print(f" Leyendo secuencia desde: {ruta_entrada}")

    try:
        with open(ruta_entrada, "r") as f:
            secuencia = f.read().strip()
    except FileNotFoundError:
        print(f" Error: No se pudo leer el archivo {ruta_entrada}")
        return

    print(f" Secuencia cargada: {secuencia}")

    # 2. Crear objeto de traducción
    obj = SecuenciaAminoacido(secuencia)

    # 3. Validar secuencia
    print(" Validando secuencia ARN...")
    try:
        obj.validar()
        print(" Secuencia válida (solo A,U,C,G y longitud múltiplo de 3).")
    except ValueError as e:
        print(f" Error de validación: {e}")
        return

    # 4. Traducir ARN → aminoácidos (1 letra)
    print(" Traduciendo codones a aminoácidos (1 letra)...")
    obj.traduceARNtoAminoacido()
    print(f"   Resultado (1 letra): {obj.st_secuenciaAminoacido}")

    # 5. Convertir a formato 3 letras
    print(" Convirtiendo a formato 3 letras...")
    obj.convertir_a_3_letras()
    print(f"   Resultado (3 letras): {obj.st_secuenciaAminoacido}")

    # 6. Guardar salida TXT
    ruta_salida_txt = "resultados/salida_3_letras.txt"
    print(f" Guardando salida TXT en: {ruta_salida_txt}")
    with open(ruta_salida_txt, "w") as f:
        f.write(obj.st_secuenciaAminoacido)

    # 7. Guardar salida CSV con cabecera
    ruta_salida_csv = "resultados/exp01-salida.csv"
    print(f" Guardando salida CSV en: {ruta_salida_csv}")

    lista_aminoacidos = obj.st_secuenciaAminoacido.split("-")

    with open(ruta_salida_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["posicion", "aminoacido_3_letras"])
        for i, aa in enumerate(lista_aminoacidos, start=1):
            writer.writerow([i, aa])

    # 8. Registrar runlog
    ruta_runlog = "resultados/runlog.txt"
    print(" Actualizando runlog...")

    with open(ruta_runlog, "a") as log:
        log.write("\n==============================\n")
        log.write(f"Fecha y hora: {datetime.datetime.now()}\n")
        log.write(f"Secuencia ARN: {secuencia}\n")
        log.write(f"Aminoácidos (3 letras): {obj.st_secuenciaAminoacido}\n")
        log.write(f"Salida TXT: {ruta_salida_txt}\n")
        log.write(f"Salida CSV: {ruta_salida_csv}\n")
        log.write("Mensajes de salida mejorados y ejecución completada.\n")
        log.write("==============================\n")

    print(" Ejecución completada correctamente.")
    print("====================================")


if __name__ == "__main__":
    main()