import pandas as pd


orders_read = pd.read_csv("Продажи_сентябрь.csv")
orders = pd.DataFrame(orders_read)

print(orders)

pivot = orders.pivot_table(index='Клиент', columns='Товар', values='Сумма', aggfunc='sum')
pivot.fillna(0, inplace=True)
print(pivot)

sum_grad = orders.groupby("Город").agg(
    Сумма=("Сумма", "sum"),
    Сред_сумма=("Сумма", "mean"),
    Количество=("Сумма", "count")
)

print("Сумма заказов по городам: \n", sum_grad)
sum_grad.to_csv("Продажи_сентябрь_города.csv", index=False)
pivot.to_csv("Продажи_сентябрь_клиент.csv", index=False)


