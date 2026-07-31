import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load and sort data
data = pd.read_csv("data/formatted_sales_data.csv")
data = data.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f7f5f2",
        "padding": "40px",
        "minHeight": "100vh"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#d6336c",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Explore Pink Morsel sales trends by region",
            style={
                "textAlign": "center",
                "color": "#555",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "30px"
            },
            children=[
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    style={"fontSize": "18px"},
                    inputStyle={"marginRight": "6px", "marginLeft": "16px"}
                )
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "borderRadius": "12px",
                "padding": "20px",
                "boxShadow": "0px 2px 10px rgba(0,0,0,0.1)",
                "maxWidth": "1000px",
                "margin": "0 auto"
            },
            children=[
                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["Region"] == selected_region]

    fig = px.line(
        filtered_data,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})",
        labels={"Date": "Date", "Sales": "Sales ($)"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial, sans-serif", size=13),
        title_font=dict(size=18, color="#d6336c")
    )
    fig.update_traces(line_color="#d6336c")

    return fig


if __name__ == "__main__":
    app.run(debug=True)