
def personal_sum(numbers):
    """ Функция personal_sum(numbers):
    Должна принимать коллекцию numbers.
    Подсчитывать сумму чисел в numbers путём перебора и увеличивать
    переменную result.
    Если же при переборе встречается данное типа отличного от числового,
    то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
    В конечном итоге функция возвращает кортеж из двух значений:
    result - сумма чисел, incorrect_data - кол-во некорректных данных. """
    sum_ = 0
    incorrect_data = 0
    for i in numbers:
        try:
            sum_ += i
        except TypeError:
            print('В numbers записан некорректный тип данных')
            incorrect_data += 1
    return sum_, incorrect_data

def calculate_average(numbers):
    """ Функция calculate_average(numbers)
        Среднее арифметическое - сумма всех данных делённая на их количество.
        Должна принимать коллекцию numbers и возвращать: среднее арифметическое
        всех чисел.
        Внутри для подсчёта суммы используйте функцию personal_sum написанную
        ранее.
        Т.к. коллекция numbers может оказаться пустой, то обработайте
        исключение ZeroDivisionError при делении на 0 и верните 0.
        Также в numbers может быть записана не коллекция, а другие типы данных,
        например числа. Обработайте исключение TypeError выводя строку
        'В numbers записан некорректный тип данных'. В таком случае функция
        просто вернёт None. """
    try:
        data = personal_sum(numbers)
    except TypeError:
        return None
    # Количество числовых элементов в коллекции numbers
    numbers_quantity = len(numbers) - data[1]
    try:
        average = data[0] / numbers_quantity
        return average
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
