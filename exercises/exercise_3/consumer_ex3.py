from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="order-splitter",
    auto_offset_reset="earliest",
)

orders_topic = app.topic(name="orders", value_deserializer="json")

sdf = app.dataframe(topic=orders_topic)


def order_output(order):
    print(f"Input: {order}")
    total = 0
    for product in order["products"]:
        print(
            f"Product: {product["name"]} quantity: {product["quantity"]} Price: {product["price"]}"
        )
        total = product["quantity"] * product["price"] + total
    print(f"Total price: {total:.2f}")
    print("")


sdf.update(order_output)


if __name__ == "__main__":
    app.run()
