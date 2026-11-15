def fibonacci():

    a, b = 0, 1
    while True:
        yield a # возвращает число и засыпает до следующего вызова
        a, b = b, a + b # сдвиг: следующее a = b, следующее b = a + b
#создаём генератор
fib = fibonacci()

for _ in range(10):
    print(next(fib), end=" ")# next() просит следующее число