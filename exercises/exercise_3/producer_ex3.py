from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parent / "data"

# print(data_path)

with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)

# pprint(orders)

# a form of entry point for interacting with Kafka, localhost:9092 is port mapped to broker container
app = Application(broker_address="localhost:9092", consumer_group="order-splitter")

orders_topic = app.topic(name="orders", value_serializer="json")

# print(jokes_topic)


def main():
    with app.get_producer() as producer:
        # print(producer)

        for order in orders:

            kafka_msg = orders_topic.serialize(key=order["order_id"], value=order)

            print(f"Produced message: key = {kafka_msg.key} value = {kafka_msg.value}")

            producer.produce(
                topic="orders", key=str(kafka_msg.key), value=kafka_msg.value
            )


if __name__ == "__main__":
    # pprint(jokes)
    main()
