# Funcionamiento
La interfaz inicial del programa se ve de la siguiente manera (para usar el programa desde internet http://jdbada.pythonanywhere.com/)

![image](https://user-images.githubusercontent.com/60485485/118373214-451c0080-b57b-11eb-9aff-2ee78e678ff1.png)

Su funcionamiento esta basado en devolver el cambio de forma en que se usen la menor cantidad de billetes y monedas, para ello será necesario que se ingrese una cantidad del monto total y una cantidad con la que pago el cliente.

![image](https://user-images.githubusercontent.com/60485485/118373882-aee9d980-b57e-11eb-8416-6044cf142156.png)

Posteriormente se da click en el botón pagar y se verá el resultado en número y en billetes, en el caso del cambio con centavos se especifico un redondeo de cincuenta centavos a las cantidades menores a 1 peso y mayores a 0.25 centavos.

![image](https://user-images.githubusercontent.com/60485485/118373930-ebb5d080-b57e-11eb-8650-5c9f98d4c01d.png)
![image](https://user-images.githubusercontent.com/60485485/118373944-fc664680-b57e-11eb-9426-f1bfa6c78977.png)

Si colocamos a la URL la cadena /admin podremos ingresar al panel del administrador y ver los registros de ventas guardados. Las claves de acceso son ***admin*** para los dos campos (sin comillas).
![image](https://user-images.githubusercontent.com/60485485/118374010-6121a100-b57f-11eb-8200-3d662f8370e7.png)


# Utilizar el código
Para utilizar el código de este repositorio será necesario en primer lugar descargar el repositorio, ya sea clonandolo, haciendo fork o descargandolo en zip. Posteriormente se deberá crear un entorno virtual en la raíz de la carpeta ***pruebaMubit***

##### Para windows:
```
c:\>python -m venv nombre_del_entorno_virtual
```

##### Para sistemas basados en UNIX:
```
python3 -m venv nombre_del_entorno_virtual
```

Posteriormente será necesario activar el entorno virtual e instalar django
```
env\Scripts\activate
pip install django
```

Por defecto Django instalará algunos paquetes adicionales, si deseamos usar el proyecto con el gestor de base de datos MySQLite no será necesario hacer algún cambio en las configuraciones, en caso de querer guardar los registros en una base de datos distinta necesitaremos seguir las instrucciones correspondientes de la documentación de django para cada gestor de base de datos. https://docs.djangoproject.com/en/3.2/ref/settings/#databases

Debido a que la información no parece ser sensible se continuará explicando sin modificar mucho las opciones de configuración, al final hay un apartado para ***Desplegar*** en donde si es necesario cambiar todas estas configuaciones. seguido de esto serpa necesario posicionarnos a la altura del archivo manage.py ubicado en prueba técnica

![image](https://user-images.githubusercontent.com/60485485/118373716-d8563580-b57d-11eb-9725-5e1bc36a382a.png)

esto es importante ya que ejecutaremos una serie de comandos para efectuar las migraciones y posteriormente correr la aplicación:

```
cd pruebatecnica
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Si nuestra terminal luce de esta manera significa que el programa corre en el servidor incorporado.
![image](https://user-images.githubusercontent.com/60485485/118373778-253a0c00-b57e-11eb-8cc1-e58b037c1abe.png)

Para realizar modificaciones en la vista, rutas o templates bastará con guardar y volver a cargar la página para ver los cambios. Más sin embargo ejecutar cambios en la base dadatos requerirá de detener el servidor y ejecutar los comandos de migraciones.

# Despliegue de la aplicación
Para este punto decidí utilizar el servicio de [Pythonanywhere](https://www.pythonanywhere.com/) quienes proporcionan un despliegue sencillo y un plan gratuito para una solo webapp por usuario. Dentro del menú Web de nuestro dashboard daremos click en crear una nueva web app y seleccionaremos una configuración manual
![image](https://user-images.githubusercontent.com/60485485/118374250-9d093600-b580-11eb-9b49-4c85f6ebed0c.png)

La versión de python que estemos utilizando y daremos siguiente, podemos guiarnos del asistente para configurar el sitio sin menores problemas, si queremos tener más detalles sobre como desplegar la aplicación de django podemos leer la [documentación de ayuda](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject)
![image](https://user-images.githubusercontent.com/60485485/118374261-aa262500-b580-11eb-8d9b-146902b749db.png)

Como pasos generales vamos a crear un entorno virtual, instalar Django en el, instalar MySQL (debido a que el servicio gratuito no tiene otro gestor de BD de forma gratuita)

```
cd pruebaMubit
mkvirtualenv --python=/usr/bin/python3.8 pruebatecnica-virtualenv
pip install django
pip install pymysql
```
Posteriormente será necesario definir:
1. Una ruta para los archivos estáticos

![image](https://user-images.githubusercontent.com/60485485/118374575-806dfd80-b582-11eb-9f93-4b496285ebb0.png)

2. Definir el estado de la aplicación como "No debug" y especificar el host al que se conecta

![image](https://user-images.githubusercontent.com/60485485/118374614-c62ac600-b582-11eb-9054-ffdaf16605f2.png)

3. Cambiar la base de datos y sus credenciales de acceso (este ejemplo no tiene gran relevancia en temas de seguridad por lo que la clave se coloca directamente en las configuraciones).

![image](https://user-images.githubusercontent.com/60485485/118374715-4b15df80-b583-11eb-9f1f-8d38d75539f5.png)

4. Editar el archivo /pruebaMubit/pruebatecnica/venta/urls.py para que pueda acceder a los archivos estáticos

![image](https://user-images.githubusercontent.com/60485485/118374823-9c25d380-b583-11eb-8866-28d660eccd87.png)

5. Ejecutar el comando para aplicar las migraciones en la consola (menú BASH)
6. Ejecutar el comando para obtener todos los datos estáticos (imagenes, css, js, etc.)
```
python manage.py collectstatic
```
7. Editar el archivo del servidor, básicamente sin editar este archivo la aplicación no funcionará

![image](https://user-images.githubusercontent.com/60485485/118375073-fd9a7200-b584-11eb-92d5-6eb4116e4f6e.png)

Y gracias a esto finalmente podremos visualizar la aplicación corriendo en un [servidor de pythonanywhere.](http://jdbada.pythonanywhere.com/)

![image](https://user-images.githubusercontent.com/60485485/118375342-bd3bf380-b586-11eb-9577-85cccdc730ea.png)

