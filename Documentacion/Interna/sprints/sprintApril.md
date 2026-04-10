# Sprint de abril

## Duración

Inicio: 31-3-2025
Fin: 2-5-2025

## Objetivos

Este sprint inicial tiene como objetivo desarrollar un primer prototipo o prueba de concepto con una funcionalidad mínima, desplegado en el servidor de SCAYLE. Esta versión servirá como base para los sprints posteriores, a los que se irá añadiendo mayor funcionalidad hasta alcanzar la versión final.

Como resultado del sprint, se dispondrá de un servicio instalado en el entorno de SCAYLE, accesible localmente a través de una interfaz de línea de comandos básica. El usuario podrá interactuar con el modelo de lenguaje mediante el envío y recepción de mensajes de texto. En esta etapa, el modelo no contará aún con información auxiliar ni herramientas externas.

## Acciones

| Nombre | Descripción | Comportamiento esperado |
|-|-|-|
| BDG | Instalación de la base de datos orientada a grafos. | - |
| Creación BDG | Diseño y estructuración inicial de la base de datos. | - |
LLM | Instalación del modelo de lenguaje | - |
| API REST | Definición e implementación inicial de la API REST. | Será posible acceder al modelo de forma básica a través de la API. |
| Lógica | Desarrollo inicial de la lógica de negocio | El sistema permitirá acceder al LLM y ejecutar consultas a través de las interfaces disponibles. |
| CLI | Implementación de una interfaz de consola básica. | Se podrá acceder al modelo mediante una línea de comandos para pruebas.
| API BD | Definición de la interfaz de acceso a la base de datos.| - |
| Scrapeo | Normalización y conexión del sistema de scraping a la base de datos. | Se establecerá la interfaz de scraping y se implementará su comunicación con la base de datos, permitiendo iniciar el proceso de recolección de datos.
| Docker | 	Configuración del entorno mediante contenedores. | Todos los módulos estarán desplegados en contenedores independientes y configurados para comunicarse entre sí. |
| SCAYLE | Migración del proyecto al SCAYLE | Se instalará y se pondrá en archa el proyecto en el SCAYLE.
