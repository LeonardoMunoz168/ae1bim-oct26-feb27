# Sistema de Gestión de Clínicas Veterinarias

## Descripción General

Este proyecto fue desarrollado utilizando Python, SQLite y SQLAlchemy ORM como parte de una actividad académica de la asignatura Desarrollo Basado en Plataformas Web.

El sistema permite modelar y administrar una red de clínicas veterinarias, registrando información relacionada con clínicas, consultorios, veterinarios e historias clínicas generadas durante la atención de mascotas.

La implementación fue realizada utilizando el paradigma ORM (Object Relational Mapping), permitiendo representar las tablas de la base de datos mediante clases Python y gestionar las relaciones entre entidades de forma más sencilla y organizada.

---

## Tecnologías Utilizadas

- Python 3.15
- SQLite
- SQLAlchemy ORM
- Visual Studio Code
- Git y GitHub

---

## Problemática Implementada

Una empresa administra una red de clínicas veterinarias ubicadas en diferentes ciudades.

Cada clínica cuenta con varios consultorios especializados donde trabajan veterinarios responsables de generar historias clínicas para las mascotas atendidas.

El sistema desarrollado permite registrar y relacionar la siguiente información:

- Clínicas
- Consultorios
- Veterinarios
- Historias Clínicas

---

## Modelo Entidad Relación

```text
CLINICA
│
├── CONSULTORIO
│       │
│       └── VETERINARIO
│               │
│               └── HISTORIA_CLINICA
```

---

## Entidades Implementadas

### Clínica

Representa cada establecimiento veterinario.

Atributos:

- id
- nombre
- direccion
- veterinario_responsable

---

### Consultorio

Representa las áreas de atención que pertenecen a una clínica.

Atributos:

- id
- nombre
- especialidad
- clinica_id

---

### Veterinario

Representa a los profesionales que trabajan dentro de un consultorio.

Atributos:

- id
- nombres
- apellidos
- correo
- licencia
- consultorio_id

---

### Historia Clínica

Representa cada atención médica realizada a una mascota.

Atributos:

- id
- fecha_atencion
- diagnostico
- tratamiento
- mascota
- veterinario_id

---

## Relaciones Implementadas

### Clínica - Consultorio

Relación uno a muchos (1:N)

- Una clínica puede tener varios consultorios.
- Un consultorio pertenece únicamente a una clínica.

---

### Consultorio - Veterinario

Relación uno a muchos (1:N)

- Un consultorio puede tener varios veterinarios.
- Un veterinario pertenece únicamente a un consultorio.

---

### Veterinario - Historia Clínica

Relación uno a muchos (1:N)

- Un veterinario puede generar múltiples historias clínicas.
- Una historia clínica pertenece a un único veterinario.

---

## Estructura del Proyecto

```text
ae1bim-oct26-feb27
│
├── configuracion.py
├── crear_base_entidades.py
├── poblar_base.py
├── consulta_all.py
├── consulta_filter.py
├── consulta_order_by.py
├── consulta_or.py
├── consulta_and.py
├── veterinaria.db
└── README.md
```

---

## Configuración de la Base de Datos

El archivo `configuracion.py` contiene la configuración de conexión a SQLite mediante SQLAlchemy.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL_BD = "sqlite:///veterinaria.db"

engine = create_engine(URL_BD)

Session = sessionmaker(bind=engine)
session = Session()
```

---

## Creación de las Tablas

Para generar la estructura de la base de datos ejecutar:

```bash
python crear_base_entidades.py
```

Resultado esperado:

```text
Base de datos creada correctamente
```

Este proceso genera el archivo:

```text
veterinaria.db
```

y crea las tablas:

- clinica
- consultorio
- veterinario
- historia_clinica

---

## Carga de Datos

Para insertar los registros iniciales ejecutar:

```bash
python poblar_base.py
```

Resultado esperado:

```text
Datos cargados correctamente
```

Se registran:

- 3 clínicas
- 6 consultorios
- 10 veterinarios
- 20 historias clínicas

---

## Consultas Implementadas

### Consulta ALL

Archivo:

```text
consulta_all.py
```

Objetivo:

Mostrar todas las clínicas junto con el número de historias clínicas asociadas.

Método utilizado:

```python
all()
```

---

### Consulta FILTER

Archivo:

```text
consulta_filter.py
```

Objetivo:

Filtrar veterinarios pertenecientes a un consultorio específico.

Método utilizado:

```python
filter()
```

---

### Consulta ORDER BY

Archivo:

```text
consulta_order_by.py
```

Objetivo:

Ordenar veterinarios por apellido de forma ascendente.

Método utilizado:

```python
order_by()
```

---

### Consulta OR

Archivo:

```text
consulta_or.py
```

Objetivo:

Obtener historias clínicas donde la mascota sea Rocky o Luna.

Método utilizado:

```python
or_()
```

---

### Consulta AND

Archivo:

```text
consulta_and.py
```

Objetivo:

Obtener historias clínicas donde la mascota sea Rocky y el diagnóstico sea Dermatitis.

Método utilizado:

```python
and_()
```

---

## Conceptos Aplicados

Durante el desarrollo de la actividad se aplicaron los siguientes conceptos:

- Programación orientada a objetos.
- Modelado de bases de datos relacionales.
- Claves primarias.
- Claves foráneas.
- Relaciones uno a muchos.
- Integridad referencial.
- SQLAlchemy ORM.
- SQLite.
- Consultas sobre bases de datos.
- Gestión de sesiones con SQLAlchemy.
- Persistencia de datos.

---

## Aprendizajes Obtenidos

Durante el desarrollo de esta práctica se adquirieron conocimientos relacionados con:

- Configuración de entornos virtuales en Python.
- Instalación y uso de SQLAlchemy.
- Creación de modelos ORM.
- Diseño de entidades y relaciones.
- Uso de SQLite como gestor de bases de datos.
- Inserción de información mediante objetos Python.
- Creación de consultas utilizando all(), filter(), order_by(), and_() y or_().
- Comprensión de la importancia de las claves foráneas y la integridad referencial.
- Uso de Git y GitHub dentro de Visual Studio Code.

---

## Autor

**Leonardo Enrique Muñoz León**

Actividad desarrollada para la asignatura:

**Desarrollo Basado en Plataformas Web**