import paho.mqtt.client as mqtt
import json

# Diccionario para almacenar los estados de los dispositivos
estado_dispositivos = {
    "sensor_luz_1": {"value": 0, "accuracy": 0},
    "sensor_luz_2": {"value": 0, "accuracy": 0},
    "cortina_1": "cerrada",
    "cortina_2": "cerrada",
}

# Lista de temas a suscribir
temas = [
    "casa/sensor_luz/1",
    "casa/sensor_luz/2",
    "casa/cortina/1",
    "casa/cortina/2",
]

# Callback al conectar al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        for tema in temas:
            client.subscribe(tema)
            print(f"Suscrito al tema: {tema}")
    else:
        print(f"Error al conectar con código: {rc}")

# Callback al recibir mensajes
def on_message(client, userdata, msg):
    tema = msg.topic
    mensaje = msg.payload.decode("utf-8")
    
    # Procesar mensajes de sensores de luz
    if "sensor_luz" in tema:
        sensor_id = tema.split("/")[-1]
        print(f"Datos recibidos del {tema}: {mensaje}")
        try:
            data = json.loads(mensaje)
            estado_dispositivos[f"sensor_luz_{sensor_id}"] = data

            # Controlar cortinas según la luz
            if data["value"] < 50 and data["accuracy"] > 0.9:
                controlar_cortinas(client, sensor_id, "abrir")
            else:
                controlar_cortinas(client, sensor_id, "cerrar")

        except json.JSONDecodeError:
            print("Error: mensaje no es JSON válido")

    # Procesar comandos para las cortinas
    elif "cortina" in tema:
        cortina_id = tema.split("/")[-1]
        print(f"Comando recibido para cortina {cortina_id}: {mensaje}")
        estado_dispositivos[f"cortina_{cortina_id}"] = mensaje

# Función para publicar comandos de cortinas
def controlar_cortinas(client, sensor_id, accion):
    cortina_id = sensor_id  # Asocia sensores y cortinas por ID
    tema_cortina = f"casa/cortina/{cortina_id}"
    client.publish(tema_cortina, accion)
    print(f"Cortina {cortina_id} -> Acción: {accion}")

# Configuración del cliente MQTT
broker = "localhost"  
puerto = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conexión al broker
client.connect(broker, puerto, 60)

# Iniciar loop para escuchar mensajes
client.loop_forever()

