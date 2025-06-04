from collections import namedtuple

# Определяем структуру для данных автомобиля
Car = namedtuple('Car', ['color', 'year', 'engine_volume', 'car_type', 'price'])

car_data_namedtuple = {
    'Mercedes': Car('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': Car('black', 2020, 2.0, 'sedan', 55000),
    # ... и так далее для остальных машин
    'Nissan': Car('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': Car('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': Car('gray', 2019, 1.6, 'suv', 32000),
    'Kia': Car('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': Car('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': Car('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': Car('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': Car('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': Car('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': Car('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': Car('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': Car('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': Car('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': Car('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': Car('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': Car('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': Car('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': Car('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': Car('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': Car('green', 2018, 3.0, 'suv', 60000),
    'Tesla': Car('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': Car('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': Car('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': Car('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': Car('white', 2021, 2.0, 'suv', 50000),
    'GMC': Car('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': Car('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': Car('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': Car('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': Car('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': Car('silver', 2018, 5.6, 'pickup', 35000)
}

# Критерии поиска
SearchCriteria = namedtuple('SearchCriteria', ['min_year', 'min_engine_volume', 'max_price'])
search_criteria_namedtuple = SearchCriteria(2017, 1.6, 36000)

filtered_namedtuple = [
    (name, car)
    for name, car in car_data_namedtuple.items()
    if car.year >= search_criteria_namedtuple.min_year
    and car.engine_volume >= search_criteria_namedtuple.min_engine_volume
    and car.price <= search_criteria_namedtuple.max_price
]

filtered_sorted_namedtuple = sorted(filtered_namedtuple, key=lambda x: x[1].price)

print("\n--- Результаты с использованием namedtuple ---")
for name, car in filtered_sorted_namedtuple[:5]:
    print(f"{name}: {car}")