# por cada palabra: bot tuiteador de palabras.

A grosso modo: El programa lee un archivo de texto que funja como base de datos, tuitea la primera línea del archivo y envía una solicitud para publicarla como un tuit. Por último vuelve a guardar el archivo de texto sin la primera línea. Al ejecutar este programa periódicamente va descartando palabra por palabra de la base de datos.


### Pre-requisitos

Para el bot:
- Una cuenta de Twitter aplicada en donde se instalará la aplicación
- Una app de Twitter
- Obtener Twitter API Consumer Keys


Para la base de datos: 
- Un archivo de texto en codificación utf-8


Para la ejecución del bot:
- Python
- crontab para sistemas operativos GNU/Linux (Alternativa: En Windows con el comando AT o el Windows Task Scheduler)
- La librería TwitterAPI (o se puede adaptar el programa para que utilice la librería de preferencia o no utilizar alguna por supuesto)
- Una máquina que funja como servidor, es decir, capaz de estar encendida todo el tiempo si este es el propósito del bot.

### Installing

1. Descargar el programa porcadapalabra.py
2. Registrar una cuenta en Twitter
3. Registrar una app en esta cuenta de Twitter en https://apps.twitter.com/  y generar las llaves de acceso y las llaves OAuth. Información [en inglés] aquí: https://dev.twitter.com/webhooks/access-tokens
4. En el porcadapalabra.py asignar los valores a las variables (líneas 10-13) para que que almacenen las 4 llaves generadas.
5. Generar una base de datos en un archivo de texto (.txt) en codificación UTF-8. Cada palabra a tuitrear deberá ir en una línea diferente.
6. Guardar el archivo de texto en la misma carpeta del programa en python.
7. Si se utilizó GNU/Linux, configurar la instrucción en cron para configurar el tiempo en que el programa debe ser ejecutado, es decir, el tiempo en que el intervalo del bot tuitearía. Aquí una aplicación Web que te ayuda a generar la instrucción cron: https://crontab-generator.org/. El comando a ejecutar este cron job sería: python /ruta/al/bot/porcadapalabra.py
8. Una vez generada dicha instrucción, deberá ser incluida en el archivo crontab ($ crontab -e)

## Pruebas

Se puede probar el programa ejecutando con la instrucción $ python /ruta/al/bot/porcadapalabra.py

## Autor

* **Rael Albert** - *Trabajo inicial* - [ralbrt](https://github.com/ralbrt)

## Licencia

Este proyecto cuenta con una licencia MIT (https://opensource.org/licenses/MIT)
