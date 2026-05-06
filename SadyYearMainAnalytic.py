import pandas as pd
import numpy as np
import warnings

from Data.Data_loader import load_data

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

df = load_data()

df = df[df["Продукт"] != "Общий итог"]

months={
    "Продажи за Январь" : "января",
    "Продажи за Февраль" : "Февраля",
    "Продажи за Март" : "Марта",
    "Продажи за Апрель" : "Апреля",
    "Продажи за Май" : "Мая",
    "Продажи за Июнь" : "Июня",
    "Продажи за Июль" : "Июля",
    "Продажи за Август" : "Августа",
    "Продажи за Сентябрь" : "Сентября",
    "Продажи за Октябрь" : "Октября",
    "Продажи за Ноябрь" : "Ноября",
    "Продажи за Декабрь" : "Декабря"
}


for month_name, search_word in months.items():
    cols=[col for col in df.columns if search_word in col]
    df[month_name]=df[cols].sum(axis=1)

avg_january=df["Продажи за Январь"].mean()
avg_february=df["Продажи за Февраль"].mean()
avg_march=df["Продажи за Март"].mean()
avg_april=df["Продажи за Апрель"].mean()
avg_may=df["Продажи за Май"].mean()
avg_june=df["Продажи за Июнь"].mean()
avg_july=df["Продажи за Июль"].mean()
avg_august=df["Продажи за Август"].mean()
avg_september=df["Продажи за Сентябрь"].mean()
avg_october=df["Продажи за Октябрь"].mean()
avg_november=df["Продажи за Ноябрь"].mean()
avg_december=df["Продажи за Декабрь"].mean()

averages_sell_of_the_month = {
    "Январь": avg_january,
    "Февраль": avg_february,
    "Март": avg_march,
    "Апрель": avg_april,
    "Май": avg_may,
    "Июнь": avg_june,
    "Июль": avg_july,
    "Август": avg_august,
    "Сентябрь": avg_september,
    "Октябрь": avg_october,
    "Ноябрь": avg_november,
    "Декабрь": avg_december
}

best_month=max(averages_sell_of_the_month, key=averages_sell_of_the_month.get)


worst_month=min(averages_sell_of_the_month, key=averages_sell_of_the_month.get)


average_sell_for_any_month=(avg_january+avg_february+avg_march+avg_april+avg_may+avg_june+avg_july+avg_august+avg_september+avg_october+avg_november+avg_december) / 12


df["Продажи продукта за год"]=df["Продажи за Январь"]+df["Продажи за Февраль"]+df["Продажи за Март"]+df["Продажи за Апрель"]+df["Продажи за Май"]+df["Продажи за Июнь"]+df["Продажи за Июль"]+df["Продажи за Август"]+df["Продажи за Сентябрь"]+df["Продажи за Октябрь"]+df["Продажи за Ноябрь"]+df["Продажи за Декабрь"]





average_sell_product_for_year = df["Продажи продукта за год"].mean()


df.loc[df["Продажи продукта за год"] > average_sell_product_for_year, "Product relevance"] = "high"
df.loc[(df["Продажи продукта за год"] > 7000)  & (df["Продажи продукта за год"] < 23000), "Product relevance"] = "medium"
df.loc[df["Продажи продукта за год"] < 7000, "Product relevance"] = "low"






all_sells_for_entire_year = df["Продажи продукта за год"].sum(axis=0)



top_relevance_products = df[df["Product relevance"] == "high"]
medium_relevance_products = df[df["Product relevance"] == "medium"]
low_relevance_product = df[df["Product relevance"] == "low"]







January_better_than_average = df[df["Продажи за Январь"] > avg_january]
February_better_than_average = df[df["Продажи за Февраль"] > avg_february]
March_better_than_average = df[df["Продажи за Март"] > avg_march]
April_better_than_average = df[df["Продажи за Апрель"] > avg_april]
May_better_than_average = df[df["Продажи за Май"] > avg_may]
June_better_than_average = df[df["Продажи за Июнь"] > avg_june]
July_better_than_average = df[df["Продажи за Июль"] > avg_july]
August_better_than_average = df[df["Продажи за Август"] > avg_august]
September_better_than_average = df[df["Продажи за Сентябрь"] > avg_september]
October_better_than_average = df[df["Продажи за Октябрь"] > avg_october]
November_better_than_average = df[df["Продажи за Ноябрь"] > avg_november]
December_better_than_average = df[df["Продажи за Декабрь"] > avg_december]


January_worse_than_average = df[df["Продажи за Январь"] < avg_january]
February_worse_than_average = df[df["Продажи за Февраль"] < avg_february]
March_worse_than_average = df[df["Продажи за Март"] < avg_march]
April_worse_than_average = df[df["Продажи за Апрель"] < avg_april]
May_worse_than_average = df[df["Продажи за Май"] < avg_may]
June_worse_than_average = df[df["Продажи за Июнь"] < avg_june]
July_worse_than_average = df[df["Продажи за Июль"] < avg_july]
August_worse_than_average = df[df["Продажи за Август"] < avg_august]
September_worse_than_average = df[df["Продажи за Сентябрь"] < avg_september]
October_worse_than_average = df[df["Продажи за Октябрь"] < avg_october]
November_worse_than_average = df[df["Продажи за Ноябрь"] < avg_november]
December_worse_than_average = df[df["Продажи за Декабрь"] < avg_december]



grouped_by_relevance = df.groupby("Product relevance")["Продажи продукта за год"].mean()





count_products_by_relevance = df.groupby("Product relevance")["Продукт"].count()


All_sell_metrics_for_relevance_by_products = df.groupby("Product relevance")["Продажи продукта за год"].agg(
    average_sell_for_relevance = "mean",
    minimum_sell_for_relevance = "min",
    maximum_sell_for_relevance = "max"
)


sales_deviation = df["Продажи продукта за год"].to_numpy()

print("Среднее значение по формуле", np.mean(sales_deviation))
print("Типичное значение", np.median(sales_deviation))
print("Стандартное отклонение", np.std(sales_deviation))

mean = np.mean(sales_deviation)
std = np.std(sales_deviation)