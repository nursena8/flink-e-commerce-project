import time
import json
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_event():
    users = ['user_1', 'user_2', 'user_3', 'user_4']
    actions = ['view', 'click', 'add_to_cart', 'purchase']
    categories = ['electronics', 'fashion', 'books', 'home']

    return {
        "user_id": random.choice(users),
        "action": random.choice(actions),
        "category": random.choice(categories),
        "timestamp": time.time()
    }

event_limit = 100  

for _ in range(event_limit):
    event = generate_event()
    producer.send('ecommerce-events', value=event)
    print(f"Üretilen Event: {event}")
    time.sleep(0.5)  

for _ in range(event_limit):
    event = generate_event()
    try:
        producer.send('ecommerce-events', value=event)
        print(f"Üretilen Event: {event}")
        time.sleep(0.5)  
    except Exception as e:
        print(f"Error while sending message: {e}")
producer.flush()
producer.close()