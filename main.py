from kafka import KafkaConsumer
from time import sleep

consumer = KafkaConsumer('uplink.data')

while True:

    for msg in consumer:
        print(msg)

    sleep(10)
