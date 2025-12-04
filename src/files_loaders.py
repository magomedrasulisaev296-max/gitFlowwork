import pandas as pd
from pandas import read_excel


def read_csv_file(road_to_csv_file: str):
    df = pd.read_csv(road_to_csv_file)
    return df


if __name__ == "__main__":
    # Только если файлы существуют, иначе будут ошибки
    transactions_csv_df = read_csv_file(r'D:\загрузки из гугл\transactions.csv')
    print("CSV файл загружен")








def read_excel_file(road_to_excel_file: str):
    df = pd.read_excel(road_to_excel_file)
    return df


if __name__ == "__main__":
    # Только если файлы существуют, иначе будут ошибки
    transactions_csv_df = read_excel_file(r'D:\загрузки из гугл\transactions_excel.xlsx')
    print("excel файл загружен")