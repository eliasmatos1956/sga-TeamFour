# Especificación de Requerimientos de Software

# Sistema de Gestión Académica - UPLA 2026-I

---

# 1. Introducción

## 1.1 Propósito

El presente documento tiene como propósito definir los requerimientos funcionales y no funcionales del Sistema de Gestión Académica (SGA) para la Universidad Peruana Los Andes. El sistema permitirá administrar estudiantes, docentes, matrículas, calificaciones y reportes académicos.

## 1.2 Alcance

El sistema web permitirá:

- Gestión de usuarios
- Gestión de estudiantes
- Gestión de docentes
- Gestión de matrículas
- Gestión de calificaciones
- Generación de reportes

El sistema será desarrollado con Django 5.1 y Django REST Framework.

## 1.3 Definiciones

- SGA: Sistema de Gestión Académica
- API: Interfaz de Programación de Aplicaciones
- UML: Unified Modeling Language
- CRUD: Create, Read, Update, Delete

## 1.4 Referencias

- IEEE 830 Software Requirements Specification
- Documentación oficial de Django
- Scrum Guide 2020

## 1.5 Visión general

El documento describe la estructura general del sistema, sus funcionalidades, restricciones y requerimientos técnicos.

---

# 2. Descripción General

## 2.1 Perspectiva del producto

El sistema será una aplicación web académica desarrollada bajo arquitectura cliente-servidor.

## 2.2 Funciones del sistema

- Inicio de sesión
- Gestión de usuarios
- Registro de estudiantes
- Registro de docentes
- Gestión de matrículas
- Registro de calificaciones
- Reportes académicos

## 2.3 Características de usuarios

- Administrador
- Docente
- Estudiante

## 2.4 Restricciones

- Uso obligatorio de Django 5.1
- Uso de Git y GitHub
- Arquitectura basada en apps

## 2.5 Suposiciones

Se asume disponibilidad de internet y acceso a navegadores modernos.

---

# 3. Requisitos Específicos

## 3.1 Requisitos funcionales

### RF01
El sistema permitirá iniciar sesión mediante usuario y contraseña.

### RF02
El sistema permitirá registrar estudiantes.

### RF03
El sistema permitirá registrar docentes.

### RF04
El sistema permitirá gestionar matrículas.

### RF05
El sistema permitirá registrar calificaciones.

### RF06
El sistema permitirá generar reportes académicos.

## 3.2 Requisitos no funcionales

### RNF01
El sistema deberá responder en menos de 3 segundos.

### RNF02
La interfaz deberá ser responsive.

### RNF03
El sistema deberá utilizar autenticación segura.

### RNF04
El sistema deberá mantener disponibilidad continua.

---

# 4. Interfaces Externas

## 4.1 Interfaces de usuario

La interfaz será web responsive y accesible desde computadoras y dispositivos móviles.

## 4.2 Interfaces de software

- Django 5.1
- SQLite3
- Django REST Framework
- GitHub

---

# 5. Otros Requisitos

## 5.1 Seguridad

El sistema implementará autenticación y validación de usuarios.

## 5.2 Rendimiento

El sistema deberá soportar múltiples usuarios concurrentes.