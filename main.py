from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO

df = pd.read_csv("1000_Sales_Records.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])


app.layout = html.Div(style={'backgroundColor': '#f8f9fa'},  # Set the background color
    children=[
    dbc.Container([

        html.Script(src='/assets/chatbot.js'),
        html.H1(
        "Sales Data Insights",
        className='mb-5',  # Keeps margin-bottom size 5
        style={'textAlign': 'center', 'color': '#007bff', 'marginTop': '30px'}  # Adds 30px space above
    ),
    
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='category',
                    value='Item Type',
                    clearable=False,
                    options=[{'label': col, 'value': col} for col in df.columns[1:]],
                    style={'width': '100%'}
                ),
                width=4, md={'size': 4, 'offset': 4}
            )
        ], className='mb-4'),

        dbc.Row([
            dbc.Col(
                dcc.Graph(id='bar-graph-plotly', figure={}),
                width=12
            )
        ], className='mb-5'),

        dbc.Row([
            dbc.Col(
                dag.AgGrid(
                    id='grid',
                    rowData=df.to_dict("records"),
                    columnDefs=[{"field": i} for i in df.columns],
                    columnSize="sizeToFit",
                    style={'height': '400px', 'width': '100%'}
                ),
                width=12
            )
        ], className='mb-4'),
    ], fluid=True),
    
])

# Create interactivity between dropdown component and graph
@app.callback(
    Output('bar-graph-plotly', 'figure'),
    [Input('category', 'value')]
)
def update_graph(selected_category):
    # Generate the new figure based on the selected category
    figure = px.bar(
        df, x='Country', y=selected_category,
        title=f"{selected_category} Sales by Country",
        labels={'x': 'Country', 'y': selected_category},
        template='none',  # Start with a blank template
        # color_discrete_sequence=px.colors.sequential.Blues[::-1],  # Use a blue color scale
        height=500
    )

    figure.update_traces(
        marker_color='light blue',  # Change the bars to purple
        marker_line_color='white',
        marker_line_width=1.5, opacity=0.8
    )

    figure.update_layout(
        title={
            'text': f"{selected_category} Sales by Country",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            # 'font': {'size': 24, 'color': '#4a4a4a'},  # Title font size and color
        },
        font=dict(
            family="Open Sans, sans-serif",  # Font family
            size=14,
            color="#4a4a4a"  # Font color
        ),
        xaxis_tickangle=-45,
        xaxis_title="Country",
        yaxis_title=f"{selected_category} Sales",
        margin=dict(l=150, r=40, t=40, b=160),
        plot_bgcolor='#f8f9fa',  # Match the dashboard background color
        paper_bgcolor='#f8f9fa',  # Match the dashboard background color
        showlegend=False  # Hide the legend if it's not necessary
    )


    return figure




if __name__ == '__main__':
    app.run_server(debug=False, port=8002, host='0.0.0.0')


from dash import Dash, html, dcc, Input, Output  # pip install dash
import plotly.express as px
import dash_ag_grid as dag  # pip install dash-ag-grid
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import pandas as pd  # pip install pandas

import matplotlib  # pip install matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# df = pd.read_csv("1000_Sales_Records.csv")


def create_app(df):
    app = Dash(_name_, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dbc.Container(
        [
            html.H1(
                "Sales Data Insights - Demo",
                className="mb-2",
                style={"textAlign": "center"},
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                id="category",
                                value="Item Type",
                                clearable=False,
                                options=df.columns[1:],
                            )
                        ],
                        width=4,
                    )
                ]
            ),
            dbc.Row([dbc.Col([html.Img(id="bar-graph-matplotlib")], width="100%")]),
            dbc.Row(
                [
                    dbc.Col(
                        [dcc.Graph(id="bar-graph-plotly", figure={})],
                        width="100%",
                        md=6,
                    ),
                ],
                className="mt-4",
            ),
            dbc.Col(
                [
                    dag.AgGrid(
                        id="grid",
                        rowData=df.to_dict("records"),
                        columnDefs=[{"field": i} for i in df.columns],
                        columnSize="sizeToFit",
                    )
                ],
                width="100%",
                md=6,
                className="mt-4 w-full",
            ),
        ]
    )

    # Create interactivity between dropdown component and graph
    @app.callback(
        Output(component_id="bar-graph-matplotlib", component_property="src"),
        Output("bar-graph-plotly", "figure"),
        Output("grid", "defaultColDef"),
        Input("category", "value"),
    )
    def plot_data(selected_yaxis):
        # Build the matplotlib figure
        fig = plt.figure(figsize=(20, 5))
        plt.bar(df["Country"], df[selected_yaxis])
        plt.ylabel(selected_yaxis)
        plt.xticks(rotation=30)

        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
        fig_bar_matplotlib = f"data:image/png;base64,{fig_data}"

        # Build the Plotly figure
        fig_bar_plotly = px.bar(df, x="Country", y=selected_yaxis).update_xaxes(
            tickangle=330
        )

        my_cellStyle = {
            "styleConditions": [
                {
                    "condition": f"params.colDef.field == '{selected_yaxis}'",
                    "style": {"backgroundColor": "#d3d3d3"},
                },
                {
                    "condition": f"params.colDef.field != '{selected_yaxis}'",
                    "style": {"color": "black"},
                },
            ]
        }
    return app
    return fig_bar_matplotlib, fig_bar_plotly, {'cellStyle': my_cellStyle}


if _name_ == "_main_":
    df = pd.read_csv("1000_Sales_Records.csv")
    app = create_app(df)
    app.run_server(debug=False, port=8002, host="0.0.0.0")

