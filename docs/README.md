# Proyecto TraductorARN

## Objetivo del proyecto
Este proyecto implementa un traductor de secuencias ARN que:
- Valida la secuencia de entrada
- Traduce codones a aminoácidos (1 letra)
- Convierte la secuencia a formato de 3 letras estándar
- Genera salidas en TXT y CSV con cabecera
- Registra cada ejecución en un runlog
- Mantiene trazabilidad mediante un manifest de datos
- Incluye tests unitarios
- Es reproducible y versionado con Git

## Estructura del proyecto
traductorARN/
├── docs/
│   ├── README.md
│   └── manifest-datos.csv
├── scripts/
│   ├── main.py
│   ├── SecuenciaARN.py
│   ├── Diccionario.py
│   └── TraductorConstantes.py
├── datos-raw/
│   └── secuenciaARN.txt
├── resultados/
│   ├── salida_3_letras.txt
│   ├── exp01-salida.csv
│   └── runlog.txt
└── tests/
    └── test_traductorARN.py

## Entrada
El archivo de entrada es `datos-raw/secuenciaARN.txt`.

## Salidas
TXT y CSV con cabecera.

## Runlog
Registra cada ejecución, tiempo, recursos y comparación expected vs salida real.

## Errores previsibles y comportamiento esperado
1. Caracteres no válidos → ValueError
2. Longitud no múltiplo de 3 → ValueError
3. Archivo no encontrado → mensaje claro
4. Codón desconocido → error controlado

## Tests unitarios
Se ejecutan con:

python -m unittest tests/test_traductorARN.py

## Ejecución del proyecto

python scripts/main.py

## Trazabilidad
Documentada en `docs/manifest-datos.csv`.

## Autor
Pilar Sanz — Máster en Bioinformática (UAX)