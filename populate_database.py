import sqlite3
import pandas as pd

# -------------------------------
# Connect to the SQLite database
# -------------------------------
connection = sqlite3.connect("shipment_database.db")
cursor = connection.cursor()

# -------------------------------
# Read the CSV files
# -------------------------------
shipping_data_0 = pd.read_csv("data/shipping_data_0.csv")
shipping_data_1 = pd.read_csv("data/shipping_data_1.csv")
shipping_data_2 = pd.read_csv("data/shipping_data_2.csv")

# -------------------------------
# Insert products from Spreadsheet 0
# -------------------------------
product_names = shipping_data_1["product"].unique()

for product in product_names:
    cursor.execute(
        "INSERT INTO product (name) VALUES (?)",
        (product,)
    )

connection.commit()

# -------------------------------
# Create a lookup dictionary
# product name -> product id
# -------------------------------
cursor.execute("SELECT id, name FROM product")

product_lookup = {}

for product_id, product_name in cursor.fetchall():
    product_lookup[product_name] = product_id

# -------------------------------
# Merge Spreadsheet 1 and 2
# -------------------------------
merged = shipping_data_1.merge(
    shipping_data_2,
    on="shipment_identifier"
)

# -------------------------------
# Count quantity of each product
# in every shipment
# -------------------------------
grouped = (
    merged.groupby(
        [
            "shipment_identifier",
            "product",
            "origin_warehouse",
            "destination_store"
        ]
    )
    .size()
    .reset_index(name="quantity")
)

# -------------------------------
# Insert shipments
# -------------------------------
for _, row in grouped.iterrows():

    cursor.execute(
        """
        INSERT INTO shipment
        (
            product_id,
            quantity,
            origin,
            destination
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            product_lookup[row["product"]],
            int(row["quantity"]),
            row["origin_warehouse"],
            row["destination_store"]
        )
    )

connection.commit()

# -------------------------------
# Close database
# -------------------------------
connection.close()

print("Database populated successfully.")
