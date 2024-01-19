# Proyecto Data engineer end to end de transmision de datos streaming

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/Data%20engineering%20architecture.png" alt="Logo de Insight Analysts Collective" >
</p>

## Descripcion general

Este proyecto sirve como una guía completa para construir un pipeline de ingeniería de datos de principio a fin. Cubre cada etapa desde la ingestión de datos hasta el procesamiento y finalmente el almacenamiento, utilizando una pila tecnológica robusta que incluye Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark y Cassandra. Todo está contenerizado utilizando Docker para facilitar la implementación y escalabilidad.

El proyecto está diseñado con los siguientes componentes:

* Fuente de Datos: Utilizamos la API randomuser.me para generar datos de usuario aleatorios para nuestra tubería.
* Apache Airflow: Responsable de orquestar la tubería y almacenar los datos obtenidos en una base de datos PostgreSQL.
* Apache Kafka y Zookeeper: Utilizados para transmitir datos desde PostgreSQL hasta el motor de procesamiento.
* Control Center y Schema Registry: Ayudan en el monitoreo y la gestión de esquemas de nuestras transmisiones Kafka.
* Apache Spark: Para el procesamiento de datos con sus nodos maestros y trabajadores.
* Cassandra: Donde se almacenarán los datos procesados.

Lo que aprenderás:

-Configurar un pipeline con Apache Airflow.
-Transmisión de datos en tiempo real con Apache Kafka.
-Sincronización distribuida con Apache Zookeeper.
-Técnicas de procesamiento de datos con Apache Spark.
-Soluciones de almacenamiento de datos con Cassandra y PostgreSQL.
-Contenerizar toda tu configuración de ingeniería de datos con Docker.





