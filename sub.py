import paho.mqtt.client as mqtt
import json

# Configuración del broker
BROKER = "localhost"
PORT = 1883
TOPIC = "habitacion/luz"

# Función de procesamiento de mensajes
def on_message(client, userdata, msg):
    try:
        # Decodificar el mensaje JSON
        datos = json.loads(msg.payload.decode())
        print(f"Datos recibidos: {datos}")

        # Analizar los datos y tomar decisiones
        valor_luz = datos["value"]
        precision = datos["accuracy"]

        if valor_luz < 50 and precision > 0.9:
            print("Encendiendo las luces...")
        else:
            print("Apagando las luces...")
    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")

# Configuración del cliente MQTT
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_message = on_message

try:
    client.connect(BROKER, PORT)
    client.subscribe(TOPIC)
    print("Conectado al broker y suscrito al tema")
    client.loop_forever()  # Mantenerse escuchando mensajes
except KeyboardInterrupt:
    print("Suscriptor detenido")
finally:
    client.disconnect()

