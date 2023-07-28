import pika
import json
import random
import time

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=RABBITMQ_HOST,
    port=RABBITMQ_PORT,
    credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange='smart_meter', exchange_type='fanout')

while True:
    # Generate energy data
    current_time = int(time.time())
    consumption = random.uniform(0, 5)
    production = random.uniform(0, 10)
    data = {
        'timestamp': current_time,
        'consumption': consumption,
        'production': production
    }

    # Publish the data to the exchange
    channel.basic_publish(
        exchange='smart_meter',
        routing_key='',
        body=json.dumps(data)
    )

    # Delay between data updates
    time.sleep(1)

# Close the connection
connection.close()