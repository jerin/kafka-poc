from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',      # start from beginning
    group_id='my-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started. Waiting for messages...")

for message in consumer:
    print(f"✓ Received | Partition: {message.partition} | Offset: {message.offset} | Data: {message.value}")