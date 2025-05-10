import pandas as pd


def categorize(raw):
    if raw > 40000:
        return "Премиум"
    elif 40000 >= raw > 20000:
        return "Средний"
    else:
        return "Обычный"


orders_sample = pd.read_csv("orders_sample.csv")
orders = pd.DataFrame(orders_sample)

mean_order = orders.groupby('Город')['Сумма'].mean()
print("Средняя сумма заказа по каждому городу: \n", mean_order)

sum_order = orders.groupby('Город')['Сумма'].sum()
max_order = sum_order.sort_values(ascending=False).head(1)
print('Город с наибольшим общим доходом: \n', max_order)

client_order = orders.groupby('Клиент')['Товар'].count()
print('Кол-во заказов товаров по клиентам: \n', client_order)

# Используя pivot_table,
# построй таблицу, где по каждому городу показана сумма заказов
# по категориям: Книга, Ноутбук, Телефон.
cities_order = orders.pivot_table(
    index="Город",
    columns='Товар',
    values='Сумма',
    aggfunc='sum'
)
cities_order.fillna(0, inplace=True)
print('Сумма заказов товаров по каждому городу: \n', cities_order)

# Добавь колонку Категория заказа по правилам:
#
# Сумма > 40000 — "Премиум"
#
# Сумма от 20000 до 40000 — "Средний"
#
# Остальное — "Обычный"
cities_order['Сумма заказов'] = cities_order[['Книга', 'Ноутбук', 'Телефон']].sum(axis=1)
cities_order['Категория'] = cities_order['Сумма заказов'].apply(categorize)
print("Таблица с Категорией заказов: \n", cities_order)

cities_order.to_csv("Разбивка_Города_Orders", index=False)

# Статистика по клиентам
# Найди клиентов, сделавших более 3 заказов. Для них вычисли:
# общую сумму заказов
# средний чек\


