year_founded = int(input('Введи год основания вуза: '))
current_year = int(input('Введи текущий год: '))

age = current_year - year_founded
print(f'Привет! Ты учишься в ВУЗе, которому сейчас {age} лет.')

# Вычисление следующего юбилея
next_anniversary = (age // 10 + 1) * 10
next_year = year_founded + next_anniversary

print(f'Следующий юбилей твоего ВУЗа (ему исполнится {next_anniversary} лет) будет в {next_year} году.')
