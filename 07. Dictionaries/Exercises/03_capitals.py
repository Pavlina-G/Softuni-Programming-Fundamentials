def country_capital():
    countries = input().split(", ")
    capitals = input().split(", ")
    country_dict = dict(zip(countries, capitals))

    for country, capital in country_dict.items():
        print(f"{country} -> {capital}")


country_capital()
