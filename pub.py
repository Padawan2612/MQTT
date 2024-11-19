import paho.mqtt.client as mqtt
import json
import time
import random

# Configuración del broker
BROKER = "localhost"  # Cambia esto si el broker está en otro servidor
PORT = 1883
TOPIC = "habitacion/luz"

# Función para simular los datos del sensor de luz
def generar_datos_sensor():
    return {
        "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
        "event_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "value": random.randint(0, 100),  # Valor de luz aleatorio entre 0 y 100
        "accuracy": round(random.uniform(0.8, 1.0), 2)  # Precisión aleatoria entre 0.8 y 1.0
    }

# Configuración del cliente MQTT
client = mqtt.Client()

try:
    client.connect(BROKER, PORT)
    print("Conectado al broker MQTT")
    while True:
        # Generar datos y enviarlos al broker
        datos = generar_datos_sensor()
        client.publish(TOPIC, json.dumps(datos))
        print(f"Datos enviados: {datos}")
        time.sleep(5)  # Envía datos cada 5 segundos
except KeyboardInterrupt:
    print("Publicador detenido")
finally:
    client.disconnect()

