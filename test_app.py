# test_app.py
import pytest
from app import create_app
from dash.testing.application_runners import import_app
import pandas as pd

@pytest.fixture
def dash_app(mocker):
    # Mock the pd.read_csv method
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({
        'Country': ['Country1', 'Country2'],
        'Item Type': [10, 20]
    }))
    # Pass the mock DataFrame to create_app
    app = create_app(pd.read_csv("1000_Sales_Records.csv"))
    return app

def test_plot_data(dash_app):
    # Use the dash_app to test the callback
    # Use the Test Client to simulate callback triggers and test responses
    with dash_app.server.test_client() as client:
        response = client.post('/_dash-update-component', json={
            'output': 'bar-graph-matplotlib.src',
            'inputs': [{'id': 'category', 'value': 'Item Type'}]
        })
        # Assert the callback response
        assert response.status_code == 200
        # More assertions can be added to validate the response data
