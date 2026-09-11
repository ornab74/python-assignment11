from pathlib import Path

import plotly.data as pldata
import plotly.express as px

# Save the chart in the script folder.
OUTPUT = Path(__file__).resolve().parent / "wind.html"

# Load sample wind data.
df = pldata.wind(return_type="pandas")

print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

# Convert wind ranges into numbers.
df["strength"] = (
    df["strength"]
    .str.replace(r"-.*|\+", "", regex=True)
    .astype(float)
)

# Create the interactive scatter plot.
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Frequency by Strength and Direction",
    labels={
        "strength": "Wind strength (range lower bound)",
        "frequency": "Frequency",
        "direction": "Direction",
    },
)

# Adjust marker size and transparency.
fig.update_traces(marker={"size": 9, "opacity": 0.8})

# Save the chart as an HTML file.
fig.write_html(
    OUTPUT,
    auto_open=False,
    full_html=True,
    include_plotlyjs=True,
    config={"displaylogo": False, "responsive": True},
)

print(f"\nSaved interactive plot to {OUTPUT}")