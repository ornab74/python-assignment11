"""Lesson 11.1: static plotting directly from a pandas DataFrame."""
import matplotlib.pyplot as plt
import pandas as pd


data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300],
}
df = pd.DataFrame(data)

df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")
plt.tight_layout()
plt.show()

df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
plt.tight_layout()
plt.show()
