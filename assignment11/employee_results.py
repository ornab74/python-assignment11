import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# set the database path.
DB_PATH = Path(__file__).resolve().parent.parent / "db" / "lesson.db"

# get revenue by employee.
query = """
SELECT
    e.last_name,
    SUM(p.price * l.quantity) AS revenue
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
JOIN line_items AS l ON o.order_id = l.order_id
JOIN products AS p ON l.product_id = p.product_id
GROUP BY e.employee_id, e.last_name
ORDER BY revenue DESC;
"""

# run the query.
with sqlite3.connect(DB_PATH) as connection:
    employee_results = pd.read_sql_query(query, connection)

# print the results.
print(employee_results)

# create the bar chart.
ax = employee_results.plot(
    x="last_name",
    y="revenue",
    kind="bar",
    title="Revenue by Employee",
    color=["steelblue"],
    legend=False,
)

# label the axes.
ax.set_xlabel("Employee last name")
ax.set_ylabel("Revenue ($)")

# rotate the names.
plt.xticks(rotation=45, ha="right")

# fix the spacing.
plt.tight_layout()

# show the chart.
plt.show()
