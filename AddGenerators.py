def print_product(df):
    for product in df["Продукт"]:
        yield product


def product_relevance_generator(df):
    for index,row in df.iterrows():
        yield row["Продукт"], row["Product relevance"]


def top_sales_generator(df):
    for _, row in df.iterrows():

        sales = row["Продажи продукта за год"]

        if sales >= 20000:
             yield row


def low_sales_generator(df):
    for _, row in df.iterrows():

        sales = row["Продажи продукта за год"]

        if sales <= 5000:
            yield row