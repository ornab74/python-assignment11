"""Lesson 11.2: create a self-contained interactive Plotly chart."""
from pathlib import Path

import plotly.data as pldata
import plotly.express as px


df = pldata.iris(return_type="pandas")
fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="Iris Data, Sepal vs. Petal Length",
    hover_data=["petal_length"],
)
fig.write_html(Path(__file__).with_name("iris.html"), auto_open=False)
