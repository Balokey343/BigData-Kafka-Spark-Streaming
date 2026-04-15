from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, LongType

# 1. Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisSensoresRealTime") \
    .getOrCreate()

# Reducir el nivel de logs para ver la tabla clara
spark.sparkContext.setLogLevel("WARN")

# 2. Definir el esquema de los datos
schema = StructType([
    StructField("sensor_id", IntegerType(), True),
    StructField("temperature", FloatType(), True),
    StructField("humidity", FloatType(), True),
    StructField("timestamp", LongType(), True)
])

# 3. Conexión a Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .option("startingOffsets", "latest") \
    .load()

# 4. Procesar el JSON
sensor_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# 5. Salida a consola con TRIGGER para que no se apague
query = sensor_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .trigger(processingTime='5 seconds') \
    .start()

query.awaitTermination()
