import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Step 1: Load the formatted data from Task 2
data = pd.read_csv("data/formatted_sales_data.csv")

# Step 2: Sort by date, so the line chart draws left-to-right chronologically
data = data.sort_values("Date")

# Step 3: Build the line chart using Plotly Express
fig = px.line(
    data,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales ($)"}
)

# Step 4: Create the Dash app
app = Dash(__name__)

# Step 5: Define the layout (what appears on the page)
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Step 6: Run the app
if __name__ == "__main__":
    app.run(debug=True)