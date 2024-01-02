import matplotlib.pyplot as plt

years = [
    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
    2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
]
ukraine_values = [
    1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6,
    0.5, 0.4, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0,
]

usa_values = [
    0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.1, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0,
]

# Введення назви країни з клавіатури
country_name = input("Введіть назву країни (Україна або США): ").capitalize()

# Визначення даних для обраної країни
if country_name == "Україна":
    country_values = ukraine_values
    country_color = 'blue'
elif country_name == "США":
    country_values = usa_values
    country_color = 'red'
else:
    print("Невірна назва країни. Будь ласка, введіть 'Україна' або 'США'.")
    exit()

# Побудова стовпчастої діаграми
plt.bar(years, country_values, color=country_color)
plt.xlabel('Рік')
plt.ylabel('Children out of school, primary')
plt.title(f'Динаміка показника "Children out of school, primary" в {country_name}')

# Відображення діаграми
plt.show()
