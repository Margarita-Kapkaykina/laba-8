country_cap = {"Франция": "Париж", "Германия": "Берлин", "Италия": "Рим", "Испания": "Мадрид",
            }
print("a) Все страны и их столицы:")
for country, capital in country_cap.items():
    print(f"Страна: {country}, Столица: {capital}")
user_c = str(input("Введите страну: "))
if user_c in country_cap:
    capital_of_country = country_cap[user_c]
    print(f" Столица страны {user_c}: {capital_of_country}")
else:
    print(f" Страна", user_c, "не найдена в словаре.")
