def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

# Пример использования
for num in square_generator(5):
    print(num)
