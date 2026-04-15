# Pipeline de Streaming con Kafka y Spark

Este proyecto demuestra un flujo completo de datos en tiempo real.

## 🚀 Arquitectura Utilizada
* **Kafka 4.2.0 (Modo KRaft):** Se eliminó el uso de Zookeeper para optimizar recursos y utilizar la gestión nativa de metadatos.
* **Spark 3.5.1:** Procesamiento estructurado mediante micro-batches de 5 segundos.
* **Python:** Productor de datos simulando sensores de temperatura y humedad.

## 🛠️ Ejecución
1. Arrancar Kafka Server (Modo Standalone).
2. Ejecutar el productor: `python3 kafka_producer.py`.
3. Ejecutar el consumidor en Spark: `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 spark_consumer.py`.

## 📈 Resultados
El sistema procesa y muestra en consola tablas estructuradas con los datos deserializados del JSON enviado por Kafka.
