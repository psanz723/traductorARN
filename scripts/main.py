import sys
from Diccionario import diccionario_codones
from SecuenciaARN import SecuenciaARN

def leer_fasta(ruta):
    secuencias = {}
    with open(ruta) as f:
        actual_id = None
        actual_seq = ""
        for linea in f:
            linea = linea.strip()
            if linea.startswith(">"):
                if actual_id:
                    secuencias[actual_id] = actual_seq
                actual_id = linea[1:]
                actual_seq = ""
            else:
                actual_seq += linea
        if actual_id:
            secuencias[actual_id] = actual_seq
    return secuencias

def traducir(secuencia):
    arn = SecuenciaARN(secuencia)
    aminoacidos = []
    for codon in arn.codones():
        aa = diccionario_codones.get(codon, "X")
        aminoacidos.append(aa)
    return "-".join(aminoacidos)

def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py <input.fasta> <output.tsv>")
        sys.exit(1)

    entrada = sys.argv[1]
    salida = sys.argv[2]

    secuencias = leer_fasta(entrada)

    with open(salida, "w") as out:
        out.write("seq\taminoacidos\n")
        for sid, seq in secuencias.items():
            aa = traducir(seq)
            out.write(f"{sid}\t{aa}\n")

if __name__ == "__main__":
    main()