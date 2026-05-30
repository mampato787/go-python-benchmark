import time
import requests
import matplotlib.pyplot as plt  # <-- Nueva librería para graficar

# Configuración
URL = "http://localhost:8081/benchmark"
TOTAL_PETICIONES = 100

print(f"🚀 Iniciando investigación de rendimiento...")
print(f"📡 Enviando {TOTAL_PETICIONES} peticiones a {URL}\n")

tiempos = []
errores = 0

tiempo_inicio_total = time.time()

for i in range(1, TOTAL_PETICIONES + 1):
    try:
        inicio_peticion = time.time()
        respuesta = requests.get(URL)
        fin_peticion = time.time()
        
        duracion = (fin_peticion - inicio_peticion) * 1000  # ms
        tiempos.append(duracion)
        
        if respuesta.status_code == 200:
            if i % 10 == 0:
                print(f"✅ Procesadas {i}/{TOTAL_PETICIONES} peticiones... Última: {duracion:.2f} ms")
        else:
            errores += 1
            
    except requests.exceptions.ConnectionError:
        errores += 1
        print(f"❌ Error: ¿El servidor de Go está apagado?")
        break

tiempo_fin_total = time.time()
duracion_total = tiempo_fin_total - tiempo_inicio_total

# === PROCESAMIENTO DE DATOS Y ESTADÍSTICAS ===
if tiempos:
    tiempo_promedio = sum(tiempos) / len(tiempos)
    tiempo_minimo = min(tiempos)
    tiempo_maximo = max(tiempos)
    
    print("\n" + "="*40)
    print("📊 RESULTADOS DE LA INVESTIGACIÓN")
    print("="*40)
    print(f"⏱️ Tiempo total del experimento : {duracion_total:.2f} segundos")
    print(f"🚀 Peticiones exitosas          : {len(tiempos)}")
    print(f"⚡ Tiempo promedio por petición : {tiempo_promedio:.2f} ms")
    print("="*40)

    # === GENERACIÓN DEL GRÁFICO (NUEVO BLOQUE) ===
    print("\n📈 Generando gráfico de rendimiento...")
    
    plt.figure(figsize=(10, 5))
    plt.plot(tiempos, color='#00ADD8', linewidth=2, label='Tiempo de respuesta (ms)')
    plt.axhline(y=tiempo_promedio, color='red', linestyle='--', label=f'Promedio ({tiempo_promedio:.2f} ms)')
    
    plt.title('Rendimiento del Servidor Go - Tiempo de Respuesta por Petición', fontsize=14, fontweight='bold')
    plt.xlabel('Número de Petición', fontsize=12)
    plt.ylabel('Tiempo de Respuesta (ms)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    # Guardamos el gráfico en la carpeta data de la raíz
    ruta_grafico = "../data/resultado_rendimiento.png"
    plt.savefig(ruta_grafico, dpi=300)
    print(f"💾 ¡Gráfico guardado exitosamente en: {ruta_grafico}!")
