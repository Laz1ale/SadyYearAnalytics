import typer

from SadyYearMainAnalytic import (
    Year_Stats,
    top_relevance_products,
    low_relevance_products,
    sales_deviation,
    df,
    best_month,
    worst_month,
    average_sell_for_any_month,
    average_sell_product_for_year,
    all_sells_for_entire_year,
    count_products_by_relevance
)

from Graphs import changes_by_sales_months
from Graphs import top_10_products_graph
from Graphs import pie_graph_by_relevance
from Graphs import pie_graph_by_brands_of_products

from AddGenerators import (
    print_product,
    product_relevance_generator,
    top_sales_generator,
    low_sales_generator
)

app = typer.Typer()


@app.command()
def stats():
    """
    Полная статистика за год
    """

    Year_Stats()


@app.command()
def product_list():
    """
    Список всех продуктов
    """

    for product in print_product(df):
        print(product)


@app.command()
def best_sales_products():
    """
    Лучшие продукты по продажам
    """

    for row in top_sales_generator(df):

        print(
            row["Продукт"],
            "-",
            row["Продажи продукта за год"]
        )


@app.command()
def worst_sales_products():
    """
    Худшие продукты по продажам
    """

    for row in low_sales_generator(df):

        print(
            row["Продукт"],
            "-",
            row["Продажи продукта за год"]
        )


@app.command()
def relevance_of_all_products():
    """
    Уровень востребованности всех продуктов
    """

    for product, relevance in product_relevance_generator(df):

        print(
            product,
            "-",
            relevance
        )


@app.command()
def deviation():
    """
    Статистика отклонений продаж
    """

    print("Среднее значение:", sales_deviation.mean())
    print("Минимальное значение:", sales_deviation.min())
    print("Максимальное значение:", sales_deviation.max())


@app.command()
def show_top_relevance_products():
    """
    Самые востребованные продукты
    """

    print(top_relevance_products)


@app.command()
def show_low_relevance_products():
    """
    Самые невостребованные продукты
    """

    print(low_relevance_products)


@app.command()
def show_best_month():
    """
    Лучший месяц по продажам
    """

    print(best_month)


@app.command()
def show_worst_month():
    """
    Худший месяц по продажам
    """

    print(worst_month)


@app.command()
def show_average_sell_for_any_month():
    """
    Средние продажи продуктов за месяц
    """

    print(average_sell_for_any_month)


@app.command()
def show_average_sell_product_for_year():
    """
    Средние продажи продукта за год
    """

    print(average_sell_product_for_year)


@app.command()
def show_all_sells_for_entire_year():
    """
    Все продажи за год
    """

    print(all_sells_for_entire_year)


@app.command()
def show_count_products_by_relevance():
    """
    Все продукты по уровням востребованности
    """

    print(count_products_by_relevance)


@app.command()
def graph_of_sells_for_months():
    changes_by_sales_months()

@app.command()
def top_10_best_products_graph():
    top_10_products_graph()

@app.command()
def relevance_part_graph():
    pie_graph_by_relevance()



@app.command()
def brands_of_products_part_of_sells_graph():
    pie_graph_by_brands_of_products()

app()