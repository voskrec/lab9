def batch_generator(iterable, size):
    # Проходим по списку с шагом size
    for i in range(0, len(iterable), size):
        # yield возвращает кусочек списка и "засыпает"
        yield iterable[i:i + size]

# Пример использования
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Разбиение на куски по 3:")
for batch in batch_generator(my_list, 3):
    print(batch)