from pathlib import Path
import json
from pprint import pprint

data_path = Path(__file__).parent / "data"

with open(data_path /"orders.json", "r") as file:
    orders = json.load(file)



total = 0
for order in orders:
    print(f"Input: {order}")
    total= 0
    for product in order["products"]:
      print(f"Product: {product["name"]} quantity: {product["quantity"]} Price: {product["price"]}")
      total = product["quantity"] * product["price"] + total
    print(f"Total price: {total:.2f}")
    print("")