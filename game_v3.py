import game_v2
import numpy as np


def guess_number(number: int, min_num = 1, max_num = 100):
    """ Угадываем число в заданном диапазоне с помощью алгоритма, основанного на бинарном поиске

    Args:
        number (int): _description_
        min_num (int, optional): Минимальное число в диапазоне в соответсвии с условиями задачи. Defaults to 1.
        max_num (int, optional): Максимальное число в соответсвии с условиями задачи. Defaults to 100.

    Returns:
        int: Число попыток
    """
    max_num +=1 #Увеличиваем верхнюю границу на 1, для корректной работы алгоритма при угадывании максимального числа
    proposed_number = (min_num+max_num)//2 #Зададим начальное значение посреди указанного в задаче диапазона
    num_try = 1 #Зададим начальное значение счетчика попыток
    while True:
        if proposed_number > number:
            max_num = proposed_number #Корректируем максимальное значение диапазона, в котором ведется поиск
            proposed_number = (proposed_number + min_num)//2 #Считаем новую середину диапазона
            num_try += 1 #Повыщаем счетчик попыток
        elif proposed_number < number:
            min_num = proposed_number #Корректируем минимальное значение диапазона, в котором ведется поиск
            proposed_number = (proposed_number + max_num)//2 #Считаем новую середину диапазона
            num_try += 1 #Повыщаем счетчик попыток
        else:
            break #Выходим из цикла, в случае нахождения числа
    return num_try #Возвращаем количество попыток


if __name__ == "__main__":
    # RUN
    game_v2.score_game(guess_number)
