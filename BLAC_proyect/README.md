Scan a page and listen to it

****** Some notes from proyect ******

gPIO conectados:

N° Funcion 
1 --> VCC 
6 --> GND 
11 -> Led 
19 -> Boton

0)Inicia todo el proceso cuando presionamos con el mouse un boton (el derecho). Para lograr esto usamos xbindkeys que está dado de alta en el archivo /etc/rc.local que se carga cuando arranca Raspbian. Al presionar el boton del mouse, se dispara la ruta que figura en el archivo /home/pi/.xbindkeysrc contenido del archivo: "sudo /home/pi/startscan" b:1

Vamos a cambiar esto para que se dispare desde un boton conectado a un GPIO utilizando Python. (button_gpio_final.py) Para esto necesito un script que voy a ejecutar en el rc.local asi corre en background. Ese script lee un puerto GPIO y ejecuta si lo presiono.
Testeo este script haciendo que si presiono el boton de GPIO se prende un led o dice algo: https://blog.330ohms.com/2020/06/17/como-conectar-un-push-button-a-raspberry-pi/

https://askubuntu.com/questions/1319516/executing-a-py-on-the-startup-to-trigger-a-gpio-button https://realpython.com/python-raspberry-pi/ https://www.engineersgarage.com/articles-raspberry-pi-python-push-button-interface-digital-input/

https://gpiozero.readthedocs.io/en/stable/ https://www.raspberrypi.org/forums/viewtopic.php?t=96424 https://www.raspberrypi.org/forums/viewtopic.php?t=270094 https://stackoverflow.com/questions/47783708/gpio-button-press-to-execute-python-3-program https://www.raspberrypi.org/forums/viewtopic.php?t=102538 https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=100722

1)Se usa el script de Paul donde se ejecuta espeak para leer un archivo llamado SCAN.txt que contiene el texto. Este texto es producto de un escaneo previo (que genera una imagen *.tiff).

Ejecuto el processcan para iniciar todo

mientras pruebo por consola solo espeak con texto: espeak -v es+f2 -k 30 -s150 -a 160 -g3 "Hola, Bienvenidos a mi nuevo proyecto electrónico. Hoy es Sábado"

probando alternativas, veo que Festival funciona mejor. se prueba: echo "Hola, Bienvenidos a mi nuevo proyecto electrónico. Hoy es Sábado" | iconv -f utf-8 -t iso-8859-1 | festival --language spanish --tts
Se escucha mejor con Festival. Instalamos nuevas voces en español: https://joenco.wordpress.com/2013/01/14/reproducir-texto-con-festival/ https://wilsonmar.github.io/iot-tts/ https://lihuen.linti.unlp.edu.ar/index.php/Festival

El problema aparece cuando se quiere leer con festival desde un archivo ya que no reproduce los acentos y la ñ. Entonces solucion: https://www.ingdiaz.org/texto-voz-ubuntu-sintesis-voz-habla/

		Script pata leer el contenido de un archivo de texto
		Crearemos un script para éste cometido. Todo en consola (y con privilegios de sudo…)

		sudo -s
		nano /usr/bin/hablar-texto

		Dentro de /usr/bin/hablar-texto agregaremos:

		cat $1 | iconv -f utf-8 -t iso-8859-1|festival --tts
		Ahora le damos los permisos respectivos.

		chmod +x /usr/bin/hablar-texto

		Ahora, verifiquemos. Digamos que tenemos un archivo de texto (/opt/leer.txt) que queremos que nos lo lea:

		hablar-texto /opt/leer.txt
https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/speak-easier-flite?view=all

Conectar automaticamente a un dispositivo BLT nuestra RPI https://wiretuts.com/connecting-bluetooth-audio-device-to-raspberry-pi
