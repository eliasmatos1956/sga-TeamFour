# ESPECIFICACIÓN DE REQUERIMIENTOS DE SOFTWARE (SRS)

## Sistema de Gestión Académica (SGA)

---

# 1. Introducción

## 1.1 Propósito

El presente documento tiene como propósito definir los requerimientos funcionales y no funcionales del Sistema de Gestión Académica (SGA) desarrollado para la Universidad Peruana Los Andes. Este sistema permitirá automatizar procesos académicos como autenticación de usuarios, matrícula estudiantil, gestión de cursos, calificaciones y generación de reportes.

---

## 1.2 Alcance

El Sistema de Gestión Académica permitirá administrar información académica de estudiantes, docentes y administradores mediante una plataforma web desarrollada con Django Framework.

El sistema incluirá módulos de:

* Gestión de usuarios
* Inicio de sesión
* Gestión académica
* Matrícula
* Registro de calificaciones
* Reportes académicos
* API REST para integración futura

---

## 1.3 Definiciones, Acrónimos y Abreviaturas

| Término | Descripción                                       |
| ------- | ------------------------------------------------- |
| SGA     | Sistema de Gestión Académica                      |
| RF      | Requisito Funcional                               |
| RNF     | Requisito No Funcional                            |
| API     | Application Programming Interface                 |
| UML     | Unified Modeling Language                         |
| IEEE    | Institute of Electrical and Electronics Engineers |

---

## 1.4 Referencias

* IEEE Std 830-1998
* Documentación oficial de Django 5.1
* Scrum Guide 2020
* Conventional Commits Specification
* GitHub Projects Documentation

---

# 2. Descripción General

## 2.1 Perspectiva del Producto

El Sistema de Gestión Académica será una plataforma web orientada a la administración académica universitaria. Permitirá centralizar procesos relacionados con estudiantes, docentes y personal administrativo.

---

## 2.2 Funciones del Producto

El sistema permitirá:

* Registro y autenticación de usuarios
* Gestión de estudiantes y docentes
* Matrícula de cursos
* Registro de notas
* Consulta de historial académico
* Generación de reportes
* Administración de roles y permisos

---

## 2.3 Características de los Usuarios

| Usuario       | Características                               |
| ------------- | --------------------------------------------- |
| Administrador | Gestiona usuarios y configuración del sistema |
| Docente       | Registra notas y consulta cursos              |
| Estudiante    | Consulta matrícula y calificaciones           |

---

## 2.4 Restricciones

* El sistema será desarrollado utilizando Python 3.12 y Django 5.1
* La base de datos inicial será SQLite
* El desarrollo seguirá metodología Scrum
* El control de versiones se realizará mediante Git y GitHub

---

# 3. Requisitos Funcionales

## RF-001 Inicio de Sesión

El sistema permitirá a los usuarios autenticarse mediante correo institucional y contraseña.

---

## RF-002 Gestión de Usuarios

El sistema permitirá al administrador registrar, modificar, eliminar y visualizar usuarios del sistema.

---

## RF-003 Gestión de Roles

El sistema permitirá asignar roles específicos a los usuarios, tales como administrador, docente y estudiante.

---

## RF-004 Registro de Estudiantes

El sistema permitirá registrar información académica y personal de estudiantes.

---

## RF-005 Registro de Docentes

El sistema permitirá registrar información de docentes y asignarles cursos correspondientes.

---

## RF-006 Gestión de Cursos

El sistema permitirá crear, editar, eliminar y visualizar cursos académicos.

---

## RF-007 Matrícula de Estudiantes

El sistema permitirá matricular estudiantes en cursos disponibles según el periodo académico.

---

## RF-008 Consulta de Matrícula

El sistema permitirá a los estudiantes consultar los cursos en los que se encuentran matriculados.

---

## RF-009 Registro de Calificaciones

El sistema permitirá a los docentes registrar y actualizar calificaciones de estudiantes.

---

## RF-010 Consulta de Calificaciones

El sistema permitirá a los estudiantes visualizar sus calificaciones registradas.

---

## RF-011 Generación de Reportes

El sistema permitirá generar reportes académicos en formato digital.

---

## RF-012 Gestión de Periodos Académicos

El sistema permitirá administrar periodos académicos activos e históricos.

---

## RF-013 Recuperación de Contraseña

El sistema permitirá recuperar contraseñas mediante validación por correo electrónico.

---

## RF-014 API REST

El sistema proporcionará servicios API REST para futuras integraciones externas.

---

## RF-015 Registro de Actividades

El sistema almacenará registros de actividades realizadas por los usuarios dentro de la plataforma.

---

# 4. Requisitos No Funcionales

## RNF-001 Rendimiento

El sistema deberá responder a solicitudes de usuarios en un tiempo máximo de 3 segundos bajo condiciones normales de uso.

---

## RNF-002 Seguridad

El sistema deberá cifrar las contraseñas de los usuarios utilizando mecanismos de seguridad proporcionados por Django Framework.

---

## RNF-003 Disponibilidad

El sistema deberá estar disponible al menos el 95% del tiempo durante el periodo académico.

---

## RNF-004 Compatibilidad

El sistema deberá ser compatible con los navegadores Google Chrome, Microsoft Edge y Mozilla Firefox.

---

## RNF-005 Usabilidad

La interfaz del sistema deberá permitir que un usuario nuevo pueda utilizar las funciones principales sin capacitación previa.

---
