import os


def file_exists(path):
    return os.path.exists(path)


def format_money(number):
    return f"{number:,.2f} ₽"



def column_exists(df, column_name):
    return column_name in df.columns

def count_products(df):
    return len(df)