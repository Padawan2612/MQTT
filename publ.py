import paho.mqtt.publish as publish
import json
import time

broker = "localhost"  

# Función para publicar datos simulados de sensores
def publicar_sensores():
    sensores = [
        {"topic": "casa/sensor_luz/1", "value": 30, "accuracy": 0.95},
        {"topic": "casa/sensor_luz/2", "value": 70, "accuracy": 0.92},
    ]
    for sensor in sensores:
        mensaje = json.dumps({"value": sensor["value"], "accuracy": sensor["accuracy"]})
        publish.single(sensor["topic"], mensaje, hostname=broker)
        print(f"Publicado en {sensor['topic']}: {mensaje}")

# Función para publicar comandos para cortinas
def publicar_comandos():
    comandos = [
        {"topic": "casa/cortina/1", "action": "abrir"},
        {"topic": "casa/cortina/2", "action": "cerrar"},
    ]
    for comando in comandos:
        publish.single(comando["topic"], comando["action"], hostname=broker)
        print(f"Publicado en {comando['topic']}: {comando['action']}")

# Publicar datos cada 5 segundos
while True:
    publicar_sensores()
    publicar_comandos()
    time.sleep(5)

