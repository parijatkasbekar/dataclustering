import pytest
from dash import Dash, dcc, html
from main import update_graph
import pandas as pd 
 
@pytest.fixture
def example_data():
    return {
        'Country': ['Libya', 'Canada'],
        'Item Type': ['Cosmetics', 'Vegetables'],
        'Sales': [3692591.20, 464953.08],
        # ... other columns
    }
 
def test_update_graph(example_data, monkeypatch):
    # Mocking the global data for the test
    monkeypatch.setattr("main.df", pd.DataFrame(example_data))
 
    # Test if the function returns a valid Plotly figure
    selected_category = 'Item Type'
    figure = update_graph(selected_category)
   
    assert figure is not None
    assert 'data' in figure
    assert 'layout' in figure
   
    # You can add more specific tests based on the expected behavior of your function
    # For example, check if the x-axis, y-axis, or title are set correctly
    assert figure['layout']['xaxis']['title']['text'] == 'Country'
    assert figure['layout']['yaxis']['title']['text'] == f"{selected_category} Sales"
    assert figure['layout']['title']['text'] == f"{selected_category} Sales by Country"
   
    # Check if the data points are correctly represented in the plot
