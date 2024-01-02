import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar

# Зчитуємо дані з нового файлу CSV
data = pd.read_csv("comptage_velo_2018.csv", parse_dates=["Date"], dayfirst=True)

# Створюємо графік для кожної велодоріжки
plt.figure(figsize=(10, 5))
for column in data.columns[2:]:
    plt.plot(data["Date"], data[column], label=column)

plt.title('Загальна популярність велодоріжок за кожен день')
plt.xlabel('Дата')
plt.ylabel('Популярність')

# Змінюємо формат позначень на осі x, щоб відображалися назви місяців
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

plt.legend()
plt.grid(True)
plt.show()

# Конвертуємо стовпець "Date" у формат дати з рядка у форматі "%d/%m/%Y" та додаємо стовпець місяця
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data["Month"] = data["Date"].dt.month

# Обчислюємо загальну популярність велодоріжок у кожному місяці, знаходимо найпопулярніший місяць загалом
sum_total = data.groupby("Month")[["Berri1","Boyer","Boyer 2","Brébeuf","Christophe-Colomb","CSC (Côte Sainte-Catherine)","Eco-Display Parc Stanley","Eco-Totem - Métro Laurier","Edmond Valade","Gouin / Lajeunesse","Maisonneuve_2","Maisonneuve_3","Notre-Dame","Parc","PierDup","Pont Jacques-Cartier","Rachel / Hôtel de Ville","Rachel / Papineau","René-Lévesque","Saint-Antoine","Saint-Laurent/Bellechasse","Saint-Urbain","Viger"]].sum().sum(axis=1)
most_popular_month_in_total = sum_total.idxmax()

print(f"\nНайпопулярніший місяць у велосипедистів: {most_popular_month_in_total} з кількістю : {sum_total.max()}")

