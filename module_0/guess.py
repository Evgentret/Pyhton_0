import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(min_digit, max_digit+1)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(min_digit, max_digit+1)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Алгоритм использует метод деления отрезка пополам: мы всегда ищем в пределах половины оставшегося
    даиапзона. Для этого каждый раз к предположению добавлям половину от разницы между верхней и нижней границами
    искомого диапазона (или вычитаем, в зависимости от того, больше или меньшен загаданного числа).

    Единственный недостаток этого алгоритма - он тяжело определяет крайние позиции диапазона из-за
    особенностей целочисленного деления, поэтому если разница между верхней и нижней границей диапазона
    равна единице, то мы просто меняем предположение на 1"""
    count = 1
    predict = max_digit // 2
    max_num = max_digit
    min_num = min_digit
    while number != predict:
        count += 1
        if number > predict:
            min_num = predict
            predict = predict + ((max_num - min_num) // 2)
            if max_num - min_num == 1:
                predict = predict + 1

        elif number < predict:
            max_num = predict
            predict = predict - ((max_num - min_num) // 2)
            if max_num - min_num == 1:
                predict = predict - 1

    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(min_digit, max_digit+1, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"... угадывает число в среднем за {score} попыток")
    return score


def user_input():
    """Запрашиваем два числа. Если ввод не нравится - берем значения по умолчанию"""

    while True:
        guess_range = input("Введите, пожалуйста, два числа диапазона (по умолчанию от 1 до 100) ").split()

        if len(guess_range) != 2:
            print(" Будет использован диапазон от 1 до 100")
            return 1, 100

        x1, x2 = guess_range

        if not (x1.isdigit()) or not (x2.isdigit()):
            print("Введите два десятичных целых числа ")
            continue

        x1, x2 = int(x1), int(x2)

        """Если пользователь перепутал максимальное и минимальное - меняем их местами"""
        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2


print ('\nВас приветствует программа сравнения работы разных алгоритмов угадывания чисел')

min_digit, max_digit = user_input()


print ('\nАлгоритм "пальцем в небо" или перебор случайных вариантов:')
score_game(game_core_v1)
print ('\nУлучшенный алгоритм случайной выборки, учитывающий "больше-меньше":')
score_game(game_core_v2)
print ('\nАлгоритм, в котором мы каждый раз делим предполагаемый диапазон пополам:')
score_game(game_core_v3)
print ('\nСпасибо за внимание!')