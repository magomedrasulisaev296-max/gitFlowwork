import pandas as pd
from pandas import read_excel


def read_csv_file(road_to_csv_file: str):
    df = pd.read_csv(road_to_csv_file)
    return df.to_dict('records')


def read_excel_file(road_to_excel_file: str):
    df = pd.read_excel(road_to_excel_file)
    return df.to_dict('records')




