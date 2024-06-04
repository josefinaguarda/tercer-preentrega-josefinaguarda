# Nombre del Proyecto: Tercer pre-entrega. 

MascotaWeb es una plataforma de adopción de mascotas diseñada para facilitar el proceso de encontrar un hogar para mascotas necesitadas. Esta aplicación web permite a los refugios listar sus mascotas disponibles para adopción y a los usuarios interesados navegar y adoptar mascotas.

## Tabla de Contenidos

1. Descripción
2. Características
3. Instalación
4. Uso
5. Tecnologías Utilizadas
6. Contribuir
7. Autores
8. Mejoras futuras

## Descripción

Esta app web fue creada como proyecto de CoderHouse 2024. 
Cuenta con dos aplicaciones:
- mi_aplicacion : con mascotas y refugios.
- adopcion: con adoptantes y adopcion. 

## Características

- Lista de mascotas disponibles para adopción con información detallada de cada mascota (nombre, edad, sexo, descripción, refugio en el que se encuentran).
- Formulario de mascotas, para agregar nuevas mascotas.
- Lista de refugios en Santa Fe Capital con informacion detallada (nombre, direccion y telefono).
- Formulario de refugios, para agregar nuevos refugios.
- Registro, Login y Logout de Usuarios.
- Desde admin/ el usuario tambien puede subir un avatar(foto) e informacion personal(celular) o realizar una adopcion. 
- Página de contacto para comunicación directa (Whatsapp). 

## Instalación

### Prerrequisitos

- Python 3.x
- Django 3.x o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/josefinaguarda/tercer-preentrega-josefinaguarda.git
    cd tercer-preentrega-josefinaguarda
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv. venv

    ```
3. Activa el entorno virtual en Windows o Linux o Mac:
    ```bash
    .\venv\Scripts\activate
    source .venv/bin/activate
    ```
4. Instala Django:
    ```bash
    pip install django
    ```

5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

6. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

7. Crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

8. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

9. Abre tu navegador y visita `http://127.0.0.1:8000/` para ver la aplicación en acción.

## Uso

- **Inicio de Sesión:** Los usuarios pueden registrarse, iniciar y cerrar sesión.
- **Administración de Refugios:** Los usuarios pueden agregar, editar y eliminar información de los refugios.
- **Adopciones:** Los usuarios pueden ver la lista de mascotas disponibles y solicitar la adopción de una mascota. De todos modos, hay restriccion para aquellas mascotas que ya fueron adoptadas, osea no se podra adoptar una mascota que ya tiene un adoptante asignado. 

## Tecnologías Utilizadas

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Base de Datos:** SQLite (por defecto, pero puede ser reemplazada por PostgreSQL, MySQL, etc.)

## Contribuir

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en el repositorio original.

## Autores

- Comisión: 54140
- Alumno: Josefina Guarda.

# Mejoras futuras

- Mejorar la presentacion de la app web con mas botones para volver o regresar, para no tener que estar usando la barra de navegacion. 

# VIDEO enlace

- Enlace del video demostrativo via Google Drive, el video no tiene auidio ya que no cuento con un microfono. 
- (https://drive.google.com/drive/folders/1Q5KNOCKy2oo3ygowvIlLgJbbOTl3peVJ?usp=sharing)

# Para entrar a mi admin:

- Usuario: jose1
- Contraseña: 1234