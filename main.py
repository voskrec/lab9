text = "Яблоко банан яблоко апельсин яблоко банан"

words = text.lower().split()  # в список слов
freq = {w: words.count(w) for w in set(words)}  # считаем частоту
result = max(freq, key=freq.get)  # самое частое слово

print(f"Самое частое: '{result}' ({freq[result]} раз)")