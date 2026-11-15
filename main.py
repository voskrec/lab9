# Создаем пустой словарь (телефонную книгу)
phonebook = {}

#  Добавление контакта
phonebook["Анна"] = "+7 900 123 45 67"
phonebook["Иван"] = "+7 911 765 43 21"

#  Поиск контакта
name= "Анна"
if name in phonebook:
    print(f"Телефон {name}: {phonebook[name]}")
else:
    print("Контакт не найден")

#  Удаление контакта
# Метод pop безопасно удаляет
phonebook.pop("Иван")

print("Текущая книга:", phonebook)