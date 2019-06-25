## Departamento de ingeniería en sistemas de información.
### Universidad Tecnología Nacional – Regional La Plata.

![Sistemas 2014](https://subefotos.com/ver/?f3d07f91914f623fee1016eeeb714d4co.png)

En el año 2013 / 2014, desempeñe tareas administrativas para el departamento de ingeniería en sistemas de información, como becario de dicho departamento. En un momento, surgió la necesidad de tener un sitio web propio, autoadministrable, que le permita a cualquier usuario registrado, la posibilidad de subir contenido al mismo.

Si bien el proyecto original no se encontraba dividido en apps o módulos, permitía registrar los siguientes modelos de datos. Por modelo, hacerlo mención a las tablas, las cuales son creadas gracias al ORM de Django.

## Modulos o apps (aplicaciones)

1. Anuncios
	- [x] Categoria
	- [x] Novedad
	- [x] Evento
	- [x] Faq (Preguntas frecuentes)
2. Academicos
	- [ ] Ps (Practica supervisada)
	- [x] Materias
	- [ ] Aulas
3. Documentos
	- [x] Programa (Syllabus)
4. Usuarios
	- [x] Autoridades
	- [ ] Alumnos
	- [x] Docentes
	

En ese momento, yo no manejaba del todo los sistemas de control de versiones y debido a que “deje de darle soporte” el mismo, fue reemplazado por un drupal. Sitio actual que se encuentra en el departamento de sistemas.

Les comparto el proyecto, dado que a alguien le puede servir de guía y los invito a que entre todos, podamos realizarle mejoras.

Les recomiendo instalar un entorno virtual, con las depencias, para no tener conflictos mientras trabajan con las mismas.

```sh
C:\Users\usuario> python -m venv nombre_entorno
```

## Recuerden, activar el entorno.

### En Windows por ejemplo, seria de la siguiente manera:

```sh
C:\Users\usuario> nombre_entorno\Scripts\activate
```

### Instalar dependencias del proyecto

```sh
(nombre_entorno) C:\Users\usuario> pip install -r requirements.txt
```

