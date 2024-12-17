import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'ecommerce-events',  
    bootstrap_servers='localhost:9092',  
    value_deserializer=lambda x: json.loads(x.decode('utf-8')), 
    enable_auto_commit=True, 
    group_id='ecommerce-group'  
)

print("messages are listening...")
print(consumer.topics())
for message in consumer:
    event = message.value  
    print(f"Event: {event}")