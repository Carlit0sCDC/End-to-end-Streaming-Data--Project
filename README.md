# Proyecto Data engineer end to end de transmision de datos streaming

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/Data%20engineering%20architecture.png" alt="Logo de Insight Analysts Collective" >
</p>

## Indice

1. [Descripcion general](#descripcion-general)
2. [Primeros pasos](#primeros-pasos)
3. [Etapa final](#Etapa-final)
4. [Conclusión](#Conclusión)

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

## Primeros pasos

En primera instancia lo primero que hice fue emular un entorno operativo linux en Visual Studio Code mediante la extension WSL:Ubuntu, esto nos permite realizar la dockerizacion y manipulacion de codigos de las herramientas Apache desde la terminal de VSC de una manera mas comoda y prolija.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/1.png" alt="Logo de Insight Analysts Collective" >
</p>

En nuestro explorador de archivo podemos ver como se nos crea el entorno de Linux apartado del entorno principal, dentro del mismo vemos el directorio de Ubuntu donde tenemos las dependencias y archivos de nuestro proyecto en nuestro editor de codigo.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/2.png" alt="Logo de Insight Analysts Collective" >
</p>

Luego procedemos con la creacion de los directorios, dags, script .txt y .yml

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/3.png" alt="Logo de Insight Analysts Collective" >
</p>

Levantamos los contenedores con el comando 'sudo docker-compose up -d' donde '-d' nos ayuda a levantarlos en un segundo plano sin que quede tomada la terminal ni nos realentice tanto nuestro entorno.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/4.png" alt="Logo de Insight Analysts Collective" >
</p>

En la siguiente imagen veremos como para poder levantar las imagenes y contenedores desde docker tenemos que tener instalado en nuestro pc 'docker desktop' y luego configurar el mismo para conectarlo con el Ubuntu de Visual Studio Code.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/5.png" alt="Logo de Insight Analysts Collective" >
</p>

Una vez levantados los contenedores veremos el proceso en la terminal y en nuestra interfaz de 'docker desktop' concluido con exito.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/6.png" alt="Logo de Insight Analysts Collective" >
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/7.png" alt="Logo de Insight Analysts Collective" >
</p>

Tambien podemos hacer las comprobaciones desde los puertos 'localhost:8080' de Airflow y 'localhost:9021' de Confluent.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/9.png" alt="Logo de Insight Analysts Collective" >
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/10.png" alt="Logo de Insight Analysts Collective" >
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/11.png" alt="Logo de Insight Analysts Collective" >
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/12.png" alt="Logo de Insight Analysts Collective" >
</p>

## Etapa final

Dentro de este recorrido vimos como se fueron armando los distintos componentes del proyecto asi como el pipeline en Airflow y el cluster de nuestro Control-center en Confluent, el cual nos ayuda a gestionar y configurar los datos de manera eficaz.

Ahora llega el momento de realizar las consultas pertinentes de nuestros datos streamings recopilados desde la API web ficticia y verificar si se depositaron correctamente en CassandraDB.

* Estructura antes de la ingesta de datos:

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/13.png" alt="Logo de Insight Analysts Collective" >
</p>

* Estructura de la consulta una vez dado inicio del pipeline:

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/14.png" alt="Logo de Insight Analysts Collective" >
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/15.png" alt="Logo de Insight Analysts Collective" >
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/End-to-end-Streaming-Data--Project/blob/main/source/17.png" alt="Logo de Insight Analysts Collective" >
</p>

## Conclusión

Espero les haya servido esta pequeña demostracion de este proyecto end to end de transmision, gestion, visualizacion y depositacion de datos streaming de manera profesional y autodidacta.

Cualquier duda o consulta sobre el mismo pueden contactarme, estoy a disposicion del dia para discutir cualquier apartado sobre el proyecto, les saluda, Carlos Diaz Colodrero.


