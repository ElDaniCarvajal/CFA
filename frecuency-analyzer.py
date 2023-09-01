import argparse
from collections import Counter
import operator

def main():
    parser = argparse.ArgumentParser(description='Analyze character frequencies in a list of strings.')
    parser.add_argument('--file', type=str, required=True, help='Path to the input file containing the list of strings.')
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        cadenas = [line.strip() for line in file]

    # Encuentra la longitud máxima de las cadenas y rellénalas con espacios en blanco si es necesario
    max_length = max(len(cadena) for cadena in cadenas)
    cadenas = [cadena.ljust(max_length) for cadena in cadenas]

    frecuencias_por_posicion = [Counter() for _ in range(max_length)]

    for cadena in cadenas:
        for i, caracter in enumerate(cadena):
            frecuencias_por_posicion[i][caracter] += 1

    frecuencias_ordenadas = []
    for frecuencia in frecuencias_por_posicion:
        sorted_frecuencia = sorted(frecuencia.items(), key=operator.itemgetter(1), reverse=True)
        frecuencias_ordenadas.append(sorted_frecuencia)

    num_cadenas = len(cadenas)
    num_columnas = max_length

    for columna, frecuencias in enumerate(frecuencias_ordenadas):
        print(f"Columna {columna + 1}")
        print("-" * 20)
        for caracter, conteo in frecuencias:
            porcentaje = (conteo / num_cadenas) * 100
            print(f"{caracter}: {porcentaje:.2f}%")
        print("\n" + "-" * 20)

if __name__ == "__main__":
    main()
