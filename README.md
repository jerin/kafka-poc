# Kafka POC

A minimal proof-of-concept demonstrating Apache Kafka producer/consumer messaging using Python.

## Overview

This project simulates an order placement event stream:
- The **producer** sends 10 `order_placed` events to a Kafka topic, one per second.
- The **consumer** listens on the same topic and prints each message as it arrives.

## Prerequisites

- Python 3.7+
- Apache Kafka running locally on `localhost:9092`
- `kafka-python` package

## Setup

**1. Install the Python dependency:**

```bash
pip install kafka-python
```

**2. Install Kafka via Homebrew:**

```bash
brew install kafka
```

**3. Start Kafka (KRaft mode — no ZooKeeper required):**

```bash
# Generate a cluster ID
KAFKA_CLUSTER_ID="$(kafka-storage random-uuid)"

# Format storage
kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/kraft/server.properties

# Start Kafka
kafka-server-start /opt/homebrew/etc/kafka/kraft/server.properties
```

**4. Create the topic:**

```bash
kafka-topics --create \
  --topic my-topic \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```

## Usage

Run the consumer and producer in separate terminals.

**Terminal 1 — start the consumer:**

```bash
python consumer.py
```

**Terminal 2 — start the producer:**

```bash
python producer.py
```

The producer will send 10 messages to the `my-topic` topic. The consumer will print each one as it is received.

### Example output

**Producer:**
```
Producer started. Sending messages...
✓ Sent: {'id': 0, 'event': 'order_placed', 'item': 'Product-0', 'quantity': 1}
✓ Sent: {'id': 1, 'event': 'order_placed', 'item': 'Product-1', 'quantity': 2}
...
Done.
```

**Consumer:**
```
Consumer started. Waiting for messages...
✓ Received | Partition: 0 | Offset: 0 | Data: {'id': 0, 'event': 'order_placed', 'item': 'Product-0', 'quantity': 1}
✓ Received | Partition: 0 | Offset: 1 | Data: {'id': 1, 'event': 'order_placed', 'item': 'Product-1', 'quantity': 2}
...
```

## Project Structure

```
kafka_poc/
├── producer.py   # Publishes order_placed events to my-topic
├── consumer.py   # Subscribes to my-topic and prints incoming messages
└── README.md
```

## Configuration

| Parameter | Value | Description |
|---|---|---|
| Bootstrap server | `localhost:9092` | Kafka broker address |
| Topic | `my-topic` | Topic used for messaging |
| Consumer group | `my-consumer-group` | Group ID for the consumer |
| Offset reset | `earliest` | Consumer reads from the beginning of the topic |
