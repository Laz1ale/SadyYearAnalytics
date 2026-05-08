

def show_best_stats(func):
    def wrapper():
        stats = func()

        print("Лучшие показатели в 2025\n")
        print("Лучший продукт:", stats["best_product"])
        print("Лучший месяц:", stats["best_month"])
        print("Самые востребованные продукты", stats["top_relevance_products"])

        return stats
    return wrapper



def show_worst_stats(func):
    def wrapper():
        stats = func()

        print("Худшие показатели в 2025\n")
        print("Худший продукт:", stats["worst_product"])
        print("Худший месяц:", stats["worst_month"])
        print("Самые невостребованные продукты", stats["low_relevance_products"])

        return stats
    return wrapper


def show_all_stats(func):
    def wrapper():
        stats = func()

        print("Все показатели в 2025\n")
        print("Лучший продукт:", stats["best_product"])
        print("Лучший месяц:", stats["best_month"])
        print("Самые востребованные продукты", stats["top_relevance_products"])
        print("Худший продукт:", stats["worst_product"])
        print("Худший месяц:", stats["worst_month"])
        print("Самые невостребованные продукты", stats["low_relevance_products"])
        print("Средние продажи за год", stats["average_sales"])
        print("Все продажи продуктов за 2025", stats["total_sales"])

        return stats
    return wrapper