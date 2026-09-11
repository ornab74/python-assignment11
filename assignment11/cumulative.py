import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# set the database path.
DB_PATH = Path(__file__).resolve().parent.parent / "db" / "lesson.db"

# get the total price for each order.
query = """
SELECT
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders AS o
JOIN line_items AS l ON o.order_id = l.order_id
JOIN products AS p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# run the SQL query.
with sqlite3.connect(DB_PATH) as connection:
    df = pd.read_sql_query(query, connection)

# add the running revenue total.
df["cumulative"] = df["total_price"].cumsum()

# check the first and last rows.
print(df.head(10))
print(df.tail(10))

# create the line chart.
ax = df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    marker="o",
    title="Cumulative Revenue by Order",
    legend=False,
)

# label the axes.
ax.set_xlabel("Order ID")
ax.set_ylabel("Cumulative revenue ($)")

# fix the spacing.
plt.tight_layout()

# show the chart.
plt.show()
