PARA CORRER EL PROYECTO SE DEBE INSTALAR DIFERENTES LIBRERIAS A CONTINUACION LOS COMANDOS 
1. Instalar Mosquitto (Broker MQTT)
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
2.- libreria para el editor de python
sudo apt install gedit
3.- Instalar la libreria mqtt
source env/bin/activate
pip install paho-mqtt
------------------------------------------------------------------------------------------
###Servidor
1.-Levantamos el servidor
mosquitto_sub -h localhost -t "habitacion/luz"
###Cliente
2.-Enviamos un mensaje para comprobar que esten conectados
mosquitto_pub -h localhost -t "habitacion/luz" -m "hola MQT"

3.-Una vez hecha la conexion ejecutamos en una nueva terminal los siguientes comandos para levantar el scrip de el server
-source env/bin/activate
-python3 sub.py

4.-De la misma manera ahora con la del cliente(lo podemos ejecutar en la misma terminal del cliente que levantamos al inicio)
-source env/bin/activate
-python3 pub.py

-------------------------------------------------------------------------------
#Para ejecutar el el archivo sub2.py 
-source env/bin/activate
-python3 sub2.py

#Para ejecutar el archivo publ.py
-source env/bin/activate
-python3 publ.py

#DE ESTA MANERA EJECUTAMOS LOS SCRIPS Y CON ELLO SE MOSTRARA LA CONEXION DE MANERA AUTOMATICA 