from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Producer started. Sending messages...")

for i in range(10):
    message = {
        "id": i,
        "event": "order_placed",
        "item": f"Product-{i}",
        "quantity": i + 1
    }
    producer.send('my-topic', message)
    print(f"✓ Sent: {message}")
    time.sleep(1)

producer.flush()
producer.close()
print("Done.")