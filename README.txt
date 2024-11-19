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
-python3 sub.py