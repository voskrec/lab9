text1 = "Это простой текст для проверки"
text2 = "Текст для проверки пересечения слов"

# Приводим к нижнему регистру, разбиваем на слова и создаем множества
words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

# Пересечение (общие слова)
common_words = words1 & words2
print("Общие слова:", common_words)