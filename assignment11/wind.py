from pathlib import Path

import plotly.express as px

OUTPUT = Path(__file__).resolve().parent / "wind.html"

# Load the sample wind data and inspect the first and last rows.
df = px.data.wind()
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# Keep the original range for hover labels. Clean strength to its lower bound.
df["strength_range"] = df["strength"].astype(str)
df["strength"] = (
    df["strength_range"].str.replace("+", "", regex=False).str.split("-").str[0].astype(float)
)

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    hover_data=["strength_range"],
    title="Wind Frequency by Strength and Direction",
    labels={
        "strength": "Wind strength (range lower bound)",
        "strength_range": "Strength range",
        "frequency": "Frequency",
        "direction": "Direction",
    },
)
fig.update_traces(marker={"size": 9, "opacity": 0.8})
fig.write_html(
    OUTPUT,
    auto_open=False,
    full_html=True,
    include_plotlyjs=True,
    config={"displaylogo": False, "responsive": True},
)
print(f"\nSaved interactive plot to {OUTPUT}")
