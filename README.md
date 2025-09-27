# Patrones de arquitectura

## Proyecto general

### 🗂️ Estructura del Proyecto

```text
├── README.md
├── assets
│   ├── UML_2.jpg
│   └── UML_3.png
├── exerciseOne
│   ├── main.py
│   └── models
│       └── __init__.py
├── exerciseThree
│   ├── main.py
│   └── models
│       ├── __init__.py
│       ├── chatroom.py
│       └── user.py
└── exerciseTwo
    ├── main.py
    └── models
        ├── __init__.py
        ├── notificacion.py
        └── plataforma.py

9 directories, 15 files
```

---

### 🚀 Cómo ejecutar el proyecto

1. Instala Python 3.8+ si no lo tienes.
2. Clona el repositorio o descarga el código.
3. Navega a la carpeta del ejercicio deseado y ejecuta su `main.py`

## Ejercicio1 – (tipo de patron)

### 📚 Descripción General

[Descripción del ejercicio 1 aquí. Explica el propósito y objetivos.]

---

### 🏛️ Arquitectura y Patrón de Diseño

- **Tipo de patrón:** [Tipo, ej. Creacional]
- **Patrón seleccionado:** **Singleton**
- **Justificación profesional:**  
  [Explica por qué se eligió este patrón, beneficios, etc.]

---

### 💡 Beneficios de aplicar el (tipo de patron)

- [Lista de beneficios aquí]
- [Otro beneficio]
- [Etc.]

---

### 🛠️ Buenas prácticas aplicadas

- [Lista de buenas prácticas]
- [Otra práctica]
- [Etc.]

---

### 📝 Diagrama de Clases

[Descripción del diagrama]

![Diagrama de Clases Ejercicio1](assets/diagram_ej1.png)

---

## Ejercicio2 – Patrón Bridge

### 📚 Descripción General

Este mini-proyecto implementa una aplicación que gestiona la visualización de notificaciones en diferentes plataformas (escritorio, móvil, web) usando el **Patrón Bridge**. El objetivo es demostrar cómo aplicar buenas prácticas de arquitectura orientada a objetos para lograr un sistema flexible, escalable y fácil de mantener, permitiendo que los tipos de notificación (mensaje, alerta, advertencia, confirmación) y las plataformas de visualización varíen independientemente.

---

### 🏛️ Arquitectura y Patrón de Diseño

- **Tipo de patrón:** Estructural
- **Patrón seleccionado:** **Bridge**
- **Justificación profesional:**  
  El patrón Bridge separa la abstracción (tipos de notificación) de la implementación (plataformas de visualización), permitiendo que ambas varíen independientemente. Este enfoque reduce el acoplamiento entre clases, facilitando la extensión del sistema sin modificar código existente. Por ejemplo, se pueden agregar nuevas plataformas (como TV o consola) o tipos de notificación sin afectar las implementaciones actuales.

---

### 💡 Beneficios de aplicar el Patrón Bridge

 - Puedes crear clases y aplicaciones independientes de plataforma.
 El código cliente funciona con abstracciones de alto nivel. No está expuesto a los detalles de la plataforma.
 Principio de abierto/cerrado. Puedes introducir nuevas abstracciones e implementaciones independientes entre sí.
 Principio de responsabilidad única. Puedes centrarte en la lógica de alto nivel en la abstracción y en detalles de la plataforma en la implementación.

---

### 🛠️ Buenas prácticas aplicadas

- SOLID: SRP y OCP (nuevas plataformas/tipos sin modificar código existente).
- Clases abstractas (ABC) y métodos abstractos: evitan instancias incorrectas.
- Anotaciones de tipo y docstrings para claridad y mantenibilidad.
- Nombres de funciones claros.

---

### 📝 Diagrama de Clases

Diseño UML basado en el patron Bridge:

![Diagrama de Clases Ejercicio2](assets/UML_2.jpg)

---

## Ejercicio3 – Patrón Mediator

### 📚 Descripción General

Este mini-proyecto implementa una aplicación de chat grupal usando el **Patrón Mediator**, cumpliendo con el ejercicio 3 de la guía de actividad.  
El objetivo es demostrar cómo aplicar buenas prácticas de arquitectura orientada a objetos para lograr un sistema flexible, escalable y fácil de mantener.

---

### 🏛️ Arquitectura y Patrón de Diseño

- **Tipo de patrón:** Comportamiento
- **Patrón seleccionado:** **Mediator**
- **Justificación profesional:**  
  El patrón Mediator centraliza la comunicación entre objetos (usuarios), delegando la coordinación a un componente mediador (la clase `ChatRoom`).  
  Este enfoque elimina las referencias directas entre usuarios, lo que reduce el acoplamiento y favorece la escalabilidad y el mantenimiento.  
  Cuando se agrega o elimina un usuario, no es necesario modificar otros objetos, cumpliendo con principios SOLID como Open/Closed y Single Responsibility.

---

### 💡 Beneficios de aplicar el Patrón Mediator

- **Bajo acoplamiento:** Cada usuario sólo depende del mediador, no de los demás usuarios.
- **Alta cohesión:** La lógica de interacción está centralizada en `ChatRoom`, evitando dispersión de responsabilidades.
- **Escalabilidad:** Se pueden agregar funcionalidades, usuarios o nuevas reglas de negocio de manera sencilla y sin impacto en el resto del sistema.
- **Testabilidad:** Al estar la lógica centralizada, es más fácil escribir pruebas unitarias y validar la funcionalidad.
- **Mantenibilidad:** Los cambios futuros son localizados y seguros; la arquitectura soporta cambios evolutivos sin deuda técnica.

---

### 🛠️ Buenas prácticas aplicadas

- **Estructura modular:** Código distribuido en paquetes (`models/`) para separación de responsabilidades.
- **Tipado explícito:** Uso de anotaciones de tipo (`typing`) para mayor claridad y robustez.
- **Docstrings:** Documentación en clases y métodos para facilitar el entendimiento y onboarding de otros desarrolladores.
- **Convención de nombres:** Uso de nombres claros y en inglés, alineados a estándares de la industria.
- **Archivos auxiliares:** Diagrama UML exportado como imagen y fuente editable para facilitar documentación viva y colaboración.

---

## 📝 Diagrama de Clases

El diseño sigue UML, orientado a objetos y fiel a la implementación real:

![Diagrama de Clases](assets/UML_3.png)

---
