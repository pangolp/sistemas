## Departamento de ingeniería en sistemas de información.
### Universidad Tecnología Nacional – Regional La Plata.

En el año 2013 / 2014, desempeñe tareas administrativas para el departamento de ingeniería en sistemas de información, como becario de dicho departamento. En un momento, surgió la necesidad de tener un sitio web propio, autoadministrable, que le permita a cualquier usuario registrado, la posibilidad de subir contenido al mismo.

Si bien el proyecto original no se encontraba dividido en apps o módulos, permitía registrar los siguientes modelos de datos. Por modelo, hacerlo mención a las tablas, las cuales son creadas gracias al ORM de Django.

1. Etiqueta / categoría (sobre novedades)
2. Novedades
3. Practicas supervisadas
	- Alumnos
	- Docentes
	- Practica
4. Eventos
5. Materias
	- Ayudantes
	- Materia
	- Programa (Syllabus)
	- Aula asignada
6.	Documentación en general
7.	Preguntas frecuentes

En ese momento, yo no manejaba del todo los sistemas de control de versiones y debido a que “deje de darle soporte” el mismo, fue reemplazado por un drupal. Sitio actual que se encuentra en el departamento de sistemas.

Les comparto el proyecto, dado que a alguien le puede servir de guía y los invito a que entre todos, podamos realizarle mejoras.

Les recomiendo instalar un entorno virtual, con las depencias, para no tener conflictos mientras trabajan con las mismas.

Recuerden que en el fichero: requirements.txt podrán obtener el listado completo de las depencias y que utilizando el comando:

```sh
pip install -r requirements.txt
```

Recuerden a su vez, realizar un fork del repositorio si desean colaborar, dado que la rama master, se encontrara bloqueada.
