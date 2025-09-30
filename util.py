import pandas as pd
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

def update_dataset():
    try:
        api.dataset_download_files('benjaminlundkvist/steam-sales-historical-dataset',
                                          path='datasets',
                                          unzip=True)
        return True
    except Exception as e:
        print(e)
        return False

def clean_dataset():
    df = pd.read_csv('datasets/steam_sales.csv')

    df['#Reviews'] = (
        df['#Reviews']
        .astype(str)  # make sure everything is string
        .str.replace(",", "", regex=False)
    )

    # Convert to numeric (coerce errors to NaN) then to int
    df['#Reviews'] = pd.to_numeric(df['#Reviews'], errors='coerce').fillna(0).astype(int)

    for col in ['Discount%', 'Price (€)', 'Original Price (€)', 'Rating']:
        df[col] = pd.to_numeric(df[col], errors='coerce')


    df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')


    # Convert Fetched At to datetime
    if 'Fetched At' in df.columns:
        df['Fetched At'] = pd.to_datetime(df['Fetched At'], errors='coerce')


    # Ensure platform columns are int (0/1)
    for col in ['Windows', 'Linux', 'MacOS']:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)

    df.to_csv('datasets/steam_sales.csv', index=False)

if __name__ == '__main__':
    update_dataset()
    clean_dataset()
