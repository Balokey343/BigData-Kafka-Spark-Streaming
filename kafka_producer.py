import json
import random
import time
from kafka import KafkaProducer

def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 10),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "timestamp": int(time.time())
    }

# Configuramos el productor para su servidor local
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

print("Iniciando envío de datos... Presione Ctrl+C para detener.")

try:
    while True:
        sensor_data = generate_sensor_data()
        # Mandamos la info al canal 'sensor_data'
        producer.send('sensor_data', value=sensor_data)
        print(f"Enviado: {sensor_data}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEnvío detenido por el usuario.")
finally:
    producer.close()
