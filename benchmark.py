import time

def main():
    inicio = time.time()

    # El mismo ciclo de prueba que en Go
    contador = 0
    for i in range(100000000):
        contador += 1

    duracion = time.time() - inicio
    print(f"Tiempo en Python: {duracion:.6f} segundos")

if __name__ == "__main__":
    main()
