import Diccionario
import TraductorConstantes
from SecuenciaARN import SecuenciaAminoacido
import datetime
import csv

def main():

    # 1. Leer secuencia ARN desde archivo
    ruta_entrada = "datos-raw/secuenciaARN.txt"
    with open(ruta_entrada, "r") as f:
        secuencia = f.read().strip()

    print("📥 Secuencia ARN cargada:", secuencia)

    # 2. Crear objeto de traducción
    obj = SecuenciaAminoacido(secuencia)

    # 3. Validar secuencia
    try:
        obj.validar()
        print("✔ Validación correcta.")
    except ValueError as e:
        print("❌ ERROR:", e)
        return

    # 4. Traducir ARN → aminoácidos (1 letra)
    obj.traduceARNtoAminoacido()
    print("🔤 Aminoácidos (1 letra):", obj.st_secuenciaAminoacido)

    # 5. Convertir a formato 3 letras
    obj.convertir_a_3_letras()
    print("🔤 Aminoácidos (3 letras):", obj.st_secuenciaAminoacido)

    # 6. Guardar salida TXT
    ruta_salida_txt = "resultados/salida_3_letras.txt"
    with open(ruta_salida_txt, "w") as f:
        f.write(obj.st_secuenciaAminoacido)

    print("💾 Salida TXT guardada en:", ruta_salida_txt)

    # 7. Guardar salida CSV con cabecera
    ruta_salida_csv = "resultados/exp01-salida.csv"
    lista_aminoacidos = obj.st_secuenciaAminoacido.split("-")

    with open(ruta_salida_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["posicion", "aminoacido_3_letras"])
        for i, aa in enumerate(lista_aminoacidos, start=1):
            writer.writerow([i, aa])

    print("📊 Salida CSV guardada en:", ruta_salida_csv)

    # 8. Registrar runlog
    ruta_runlog = "resultados/runlog.txt"
    with open(ruta_runlog, "a") as log:
        log.write("\n==============================\n")
        log.write(f"Fecha y hora: {datetime.datetime.now()}\n")
        log.write(f"Secuencia ARN: {secuencia}\n")
        log.write(f"Aminoácidos (3 letras): {obj.st_secuenciaAminoacido}\n")
        log.write(f"Salida TXT: {ruta_salida_txt}\n")
        log.write(f"Salida CSV: {ruta_salida_csv}\n")
        log.write("CSV generado con cabecera estándar.\n")
        log.write("==============================\n")

    print("📝 Runlog actualizado.")


if __name__ == "__main__":
    main()