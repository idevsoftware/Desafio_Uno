# Respuesta al Desafío 1 (Períodos Perdidos)

Esta rama contiene mi solución nivel 3 en Python al desafío publicado, utilizando el microframework Flask para webapps.

## Requerimientos:

Python 3, idealmente dentro de un `virtualenv`. Para crearlo y activarlo ejecutar lo siguiente desde la raíz de la rama del repo:

```
virtualenv env
. env/bin/activate
```

La primera línea solo es necesaria la primera vez, ya que el `virtualenv` es persistente a nivel de filesystem.

## Dependencias:

Las dependencias para el proyecto (básicamente `Flask`) están listadas en el archivo de requerimientos `pip-install.txt`, en la raíz de esta rama del repo. 

Se pueden instalar usando el mismo archivo a través de `pip` desde el `virtualenv` previamente activado (paso anterior):

```
pip install -r pip-install.txt
```

## Configuración:

El proyecto incluye dos endpoints: `/` que es la solución al desafío, y `/sampledata`, ambos vía `GET`. El segundo contiene una muestra estática con datos de ejemplo, los cuales pueden ser modificados directamente al final del archivo `webapp/app/routes.py`.

Opcionalmente se puede especificar una URL distinta para obtener los datos de entrada, mediante el parámetro `DATA_URL` del archivo `webapp/config.py`.

## Ejecución:

Una vez instaladas las dependencias descritas anteriormente basta con ejecutar `flask run` desde el directorio `webapp`:

```
cd webapp/
flask run
```

El endpoint que genera la salida planteada por el desafío se encuentra entonces disponible en `http://localhost:5000/`.

## Notas:

Esta solución al desafío contiene explícitamente lo solicitado y no realiza ningún tipo de validaciones adicionales ni manejo de errores.

Se adjuntan muestras de la entrada y salida en los archivos `sampledata.json` y `sampleresponse.json`, respectivamente.
