import io
import pandas as pd
import requests
import os 


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey=a08EQHErsfdFd0YFAj4wJTRKHapTH8Io'
    response = requests.get(url)
    response.raise_for_status()


    data = response.json()

    if "results" not in data: 
        raise ValueError(f"Unexpected API response: {data}")

    df= pd.DataFrame(data["results"])
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame)
    assert not output.empty
