faculty_name = input('Введи название факультета: ').strip()

# Удаление союза "и" и разбивка на слова
words = faculty_name.replace('и', '').split()

# Создание аббревиатуры
abbreviation = ''
for word in words:
    if word:  # Проверка, что слово не пустое
        abbreviation += word[0].upper()

print(f'Аббревиатура факультета: {abbreviation}')
