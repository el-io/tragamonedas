# Tragamonedas
Este proyecto consiste en una máquina tragamonedas simple implementada con Flask, HTML, CSS y Bootstrap.

Permite a los usuarios jugar a la máquina tragamonedas, girar los rodillos y ganar premios en función de las combinaciones de símbolos obtenidas.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos y carpetas:

- **app.py**: Este es el archivo principal de la aplicación Flask que contiene la lógica para manejar las rutas y las interacciones con el usuario.
- **juego.py**: Este archivo contiene la definición de la clase Tragamonedas, que simula el funcionamiento de la máquina tragamonedas. Contiene métodos para girar los rodillos y calcular el premio.
- **templates/**: Esta carpeta contiene los archivos HTML que se utilizan para renderizar las páginas web de la aplicación.
- **static/**: Esta carpeta contiene los archivos estáticos, como hojas de estilo CSS y scripts JavaScript, que se utilizan para dar estilo y funcionalidad a las páginas web.
- **datos.db**: Esta es la base de datos SQLite que se utiliza para almacenar el saldo del jugador.

## Instalación y Ejecución

Para ejecutar el proyecto, siga los siguientes pasos:

1. Clonar el repositorio desde GitHub: `git clone <URL del repositorio>`
2. Instalar las dependencias del proyecto: `pip install -r requirements.txt`
3. Ejecutar la aplicación: `python app.py`
4. Acceda a la aplicación en su navegador web: `http://localhost:5000/`

## Funcionalidades

La aplicación tiene las siguientes funcionalidades:

- Un jugador puede iniciar el juego desde la página de inicio (index.html) haciendo clic en el botón "Girar".
- Si el jugador tiene suficiente saldo, se realizará un giro en la máquina tragamonedas y se mostrarán los resultados en la página de juego (juego.html).
- Si el jugador gana, se mostrará un mensaje de felicitación con el premio ganado.
- Si el jugador no tiene suficiente saldo para jugar, se le redirigirá a la página de inicio.
