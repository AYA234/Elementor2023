from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc, Input, Output
import random
from datetime import datetime, timedelta

app = Dash(__name__)

# Function to generate fake site usage data
def generate_fake_data():
    data = []
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    for _ in range(10):
        timestamp = end_time.strftime("%Y-%m-%d %H:%M:%S")
        if timestamp >= start_time.strftime("%Y-%m-%d %H:%M:%S"):
            storage_gb = round(random.uniform(50, 200), 2)
            disc_cache = round(random.uniform(0, 100), 2)
            disc_a_gb = round(random.uniform(100, 500), 2)
            disc_b_gb = round(random.uniform(100, 500), 2)
            cpu_percent = round(random.uniform(0, 100), 2)
            cpu_tic = round(random.uniform(0, 1000), 2)

            data.append({
                "timestamp": timestamp,
                "storage_gb": storage_gb,
                "disc_cache": disc_cache,
                "disc_a_gb": disc_a_gb,
                "disc_b_gb": disc_b_gb,
                "cpu_percent": cpu_percent,
                "cpu_tic": cpu_tic
            })

        end_time -= timedelta(weeks=1)

    return data

# Function to create a bar plot for site usage
def create_usage_chart(data):
    chart = dcc.Graph(
        figure={
            "data": [
                {
                    "x": [d["timestamp"] for d in data],
                    "y": [d["storage_gb"] for d in data],
                    "type": "bar",
                    "name": "Storage (GB)",
                },
                {
                    "x": [d["timestamp"] for d in data],
                    "y": [d["disc_cache"] for d in data],
                    "type": "bar",
                    "name": "Disk Cache",
                },
                {
                    "x": [d["timestamp"] for d in data],
                    "y": [d["disc_a_gb"] for d in data],
                    "type": "bar",
                    "name": "Disk A (GB)",
                },
                {
                    "x": [d["timestamp"] for d in data],
                    "y": [d["disc_b_gb"] for d in data],
                    "type": "bar",
                    "name": "Disk B (GB)",
                },
                {
                    "x": [d["timestamp"] for d in data],
                    "y": [d["cpu_percent"] for d in data],
                    "type": "bar",
                    "name": "CPU Percent",
                },
                {
                    "x": [d["timestamp"] for d in data],
                    "y": [d["cpu_tic"] for d in data],
                    "type": "bar",
                    "name": "CPU Tic",
                },
            ],
            "layout": {
                "title": "Site Usage",
                "xaxis": {"title": "Timestamp"},
                "yaxis": {"title": "Usage"},
                "plot_bgcolor": "#f9f9f9",
                "paper_bgcolor": "#f9f9f9",
            },
        },
    )
    return chart

# Dash application layout
app.layout = html.Div(
    id="app-container",
    children=[
        html.H1("Elementor Site Usage", style={"text-align": "center"}),
        html.Div(id="login-container", children=[
            html.Label("User ID:", style={"font-weight": "bold"}),
            dcc.Input(id="user-id-input", type="text", placeholder="Enter user ID"),
            html.Label("Password:", style={"font-weight": "bold"}),
            dcc.Input(id="password-input", type="password", placeholder="Enter password"),
            html.Button("Login", id="login-button", n_clicks=0),
            html.Div(id="login-status", children="")
        ]),
        html.Div(id="usage-container", style={"display": "none"}, children=[
            html.Div(
                children=[
                    html.Label("Select Site:", style={"font-weight": "bold"}),
                    dcc.Dropdown(
                        id="site-dropdown",
                        options=[
                            {"label": "Site 1", "value": "site1"},
                            {"label": "Site 2", "value": "site2"},
                            # Add more site options as needed
                        ],
                        value=None,
                        style={"width": "200px"},
                    ),
                ],
                style={"margin-bottom": "20px"},
            ),
            html.Div(id="usage-chart", style={"width": "800px", "margin": "0 auto"}),
        ]),
    ],
    style={"font-family": "Arial, sans-serif", "padding": "20px"},
)

# Callback function to handle user login
@app.callback(
    Output("login-status", "children"),
    Output("login-container", "style"),
    Output("usage-container", "style"),
    [Input("login-button", "n_clicks")],
    [State("user-id-input", "value"), State("password-input", "value")]
)
def handle_login(n_clicks, user_id, password):
    if n_clicks > 0:
        # Call the login function with user_id and password
        success = login(user_id, password)
        
        if success:
            # Return appropriate messages and show/hide containers
            return "Login successful!", {"display": "none"}, {"display": "block"}
        else:
            return "Invalid user ID or password", {"display": "block"}, {"display": "none"}
    
    # Default values for initial load
    return "", {"display": "block"}, {"display": "none"}

# Callback function to update the usage chart based on site selection
@app.callback(
    Output("usage-chart", "children"),
    [Input("site-dropdown", "value")]
)
def update_usage_chart(site_id):
    if site_id:
        data = generate_fake_data()
        chart = create_usage_chart(data)
        return chart
    return "No data available for the selected site."

# Dummy login function for demonstration purposes
def login(user_id, password):
    # Perform authentication logic here
    # Replace with your actual login logic or API call
    # if user_id == "admin" and password == "password":
    #     return True
    # return False
    return True

if __name__ == "__main__":
    app.run_server(debug=True)

