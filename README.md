tarea-3-redes
=============

La pregunta 1 fue desarrollada en write latex -> www.writelatex.com
Por lo que se adjunta el pdf dentro de la carpeta  "pregunta 1" junto con las imágenes utilizadas.

Se obtuvieron todas las rutas de  direcciones ingresadas en la herramienta Open Visual Traceroute a escepción de una.

Se puede observar que en el caso de la dirección de la embajada chilena en Australia (www.chile.embassy.gov.au), la herramienta no termina la ruta, debido a que esta se configuró con "timeout" 0, después de cierto tiempo esperando se debió detener con el botón con signo de "apagado".  El hecho de que la ruta no se completara pudo haber ocurrido debido a que el último router bloquea por medio de firewall los mensajes UDP y ICMP.

La ruta incompleta es considerada como la ruta obtenida para esa dirección en el informe, ya que el hecho de que esté incompleta no afecta en la investigación de "los viajes" que realizan los paquetes.


los códigos de las preguntas  restantes están en python.

La pregunta 2 posee el nombre de  tarea 3 redes. py   y genera el achivo routers.txt  en el cual se encuentra el resultado  de la pregunta 
La pregunta 3  esta bien  nombrada y su archivo de salida se llama routers_preg2.txt
