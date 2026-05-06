import pandas as pd
import os

def load_data():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "Data",
        "Отчёт за год 2025.xlsx"
    )

    df = pd.read_excel(file_path)
    return df