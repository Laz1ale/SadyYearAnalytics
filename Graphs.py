import matplotlib.pyplot as plt

from SRC.SadyYearMainAnalytic import All_Sells_Sady_Pridonya
from SadyYearMainAnalytic import month_sales
from SadyYearMainAnalytic import count_products_by_relevance
from SadyYearMainAnalytic import df
from SadyYearMainAnalytic import All_Sells_Moy
from SadyYearMainAnalytic import All_Sells_Nemoloko
from SadyYearMainAnalytic import All_Sells_Sady_Pridonya


def changes_by_sales_months():

    months = list(month_sales.keys())
    sales = list(month_sales.values())

    plt.figure(figsize=(12, 7))

    plt.plot(months,sales,marker="o")

    plt.title("Изменение продаж по месяцам")

    plt.xlabel("Месяца")


    plt.ylabel("Продажи")

    plt.grid(True)

    plt.show()



# changes_by_sales_months()




def top_10_products_graph():

    top_products = df.sort_values("Продажи продукта за год", ascending=False).head(10)

    plt.figure(figsize=(12, 7))

    plt.bar(
        top_products["Продукт"],
        top_products["Продажи продукта за год"]
    )

    plt.title("Топ 10 продуктов по продажам")

    plt.xlabel("Продукты")

    plt.ylabel("Продажи")

    plt.xticks(rotation=90)

    plt.grid(True)

    plt.show()


# top_10_products_graph()

def pie_graph_by_relevance():

    type_of_relevance = count_products_by_relevance.index

    values = count_products_by_relevance.values


    plt.figure(figsize=(8,8))


    plt.pie(
        values,
        labels=type_of_relevance,
        autopct="%1.1f%%"
    )

    plt.title("Распределение продуктов по востребованности")

    plt.show()

# pie_graph_by_relevance()



def pie_graph_by_brands_of_products():

    brands_of_products = [
        "Сады Придонья",
        "Мой",
        "Nemoloko"
    ]

    values = [
        All_Sells_Sady_Pridonya,
        All_Sells_Moy,
        All_Sells_Nemoloko
    ]

    plt.figure(figsize=(8,8))

    plt.pie(
        values,
        labels=brands_of_products,
        autopct = "%1.1f%%"
    )

    plt.title("Распределение продаж по брендам продуктов")


    plt.show()


pie_graph_by_brands_of_products()