from pathlib import Path

import plotly.data as pldata
import plotly.express as px

OUTPUT = Path(__file__).resolve().parent / "wind.html"

# load the sample wind data into pandas so I can work with it.
df = pldata.wind(return_type="pandas")
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))


# Preserve the source ranges for hover labels, then convert each range to a numeric midpoint.
df["strength_range"] = df["strength"].astype(str)
strength_midpoints = {
    "0-1": 0.5,
    "1-2": 1.5,
    "2-3": 2.5,
    "3-4": 3.5,
    "4-4": 4.0,
    "4-5": 4.5,
    "5-6": 5.5,
    "6+": 6.5,
}
df["strength"] = df["strength_range"].map(strength_midpoints).astype(float)


# Give each direction its own panel so the pattern is easier to see.
compass_order = [
    "N", "NNE", "NE", "ENE",
    "E", "ESE", "SE", "SSE",
    "S", "SSW", "SW", "WSW",
    "W", "WNW", "NW", "NNW",
]

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    facet_col="direction",
    facet_col_wrap=4,
    category_orders={"direction": compass_order},
    custom_data=["strength_range", "direction"],
    title="Wind Frequency by Strength and Direction",
    labels={
        "strength": "Wind strength",
        "frequency": "Frequency",
        "direction": "Direction",
    },
)

fig.update_traces(
    marker={"size": 9, "opacity": 0.88},
    hovertemplate=(
        "Direction: %{customdata[1]}<br>"
        "Strength range: %{customdata[0]}<br>"
        "Frequency: %{y:.1f}<extra></extra>"
    ),
)

# Give the chart enough room so the smaller panels do not feel crowded.
fig.update_layout(
    height=900,
    width=1200,
    showlegend=False,
    title={"x": 0.5, "xanchor": "center"},
    margin={"l": 70, "r": 40, "t": 90, "b": 70},
)

# Show the original strength ranges.
fig.update_xaxes(
    tickvals=list(strength_midpoints.values()),
    ticktext=list(strength_midpoints.keys()),
    title_text="Wind strength range",
)
fig.update_yaxes(title_text="Frequency", rangemode="tozero")

# keep the panel titles simple and show only the compass direction.
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

# save the finished chart as an interactive HTML file.
fig.write_html(
    OUTPUT,
    auto_open=False,
    full_html=True,
    include_plotlyjs=True,
    config={"displaylogo": False, "responsive": True},
)

print(f"\nSaved clearer interactive plot to {OUTPUT}")