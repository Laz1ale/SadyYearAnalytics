import pandas as pd
import numpy as np

from SRC.Utils import (
    format_money,
    column_exists,
    count_products
)

from SRC.AddGenerators import (
    print_product,
    product_relevance_generator,
    top_sales_generator,
    low_sales_generator
)

def test_format_money():
    result = format_money(3700)

    assert result == "3,700.00 ₽"

def test_column_exists():

    df = pd.DataFrame({
        "Цена": [300, 400]
    })

    result = column_exists(df, "Цена")

    assert result == True


def test_column_no_exists():

    df = pd.DataFrame({
        "Цена": [100, 200]
    })

    result = column_exists(df, "Продажи")

    assert result == False

def test_count_products():

    df = pd.DataFrame({
        "Продукт": ["Сок", "Вода", "Нектар"]
    })

    result = count_products(df)

    assert result == 3


def test_mean_sales():

    sales = np.array([1000, 2000, 3000])

    result = np.mean(sales)

    assert result == 2000


def test_median_sales():

    sales = np.array([1000, 2000, 3000])

    result = np.median(sales)

    assert result == 2000


def test_std_sales():

    sales = np.array([1000, 2000, 3000])

    result = round(np.std(sales), 2)

    assert result == 816.5




def test_print_product():

    df = pd.DataFrame({
        "Продукт": ["Сок", "Нектар"]
    })

    result = list(print_product(df))

    assert result == ["Сок", "Нектар"]


def test_product_relevance_generator():

    df = pd.DataFrame({
        "Продукт": ["Сок", "Нектар"],
        "Product relevance": ["high", "low"]
    })

    result = list(product_relevance_generator(df))

    assert result == [
        ("Сок", "high"),
        ("Нектар", "low")
    ]


def test_top_sales_generator():

    df = pd.DataFrame({
        "Продукт": ["Сок", "Нектар"],
        "Продажи продукта за год": [25000, 3000]
    })

    result = list(top_sales_generator(df))

    assert len(result) == 1

    assert result[0]["Продукт"] == "Сок"


def test_low_sales_generator():

    df = pd.DataFrame({
        "Продукт": ["Сок", "Нектар"],
        "Продажи продукта за год": [2000, 30000]
    })

    result = list(low_sales_generator(df))

    assert len(result) == 1

    assert result[0]["Продукт"] == "Сок"



