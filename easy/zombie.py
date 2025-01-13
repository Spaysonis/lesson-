

def attack(zombies:list[int], plants:list[int]) -> bool:

    '''
    Функция принимает два массива чисел, zombie and plants ,
    возвращает True -> если plants победил,
    возвращает False -> если zombie победил
    '''

    sum_power_plants = sum(plants)  # Сумма силы растений.
    sum_power_zombie = sum(zombies)  # Сумма силы зомби.

    len_plants = len(plants)  # Длина массива растений.
    len_zombie = len(zombies)  # Длина массива зомби.

    result_plants = 0  # Количество выживших растений.
    result_zombie = 0  # Количество выживших зомби.

    for plant, zombie in zip(plants, zombies):  #  Цикл для сравнения элементов двух массивов в порядке индексации.
        if plant > zombie:
            result_plants += 1
        elif zombie > plant:
            result_zombie += 1

    result_plants += len_plants - len_zombie  # Добавляем оставшийся элементы в случае если массив Растений был больше.
    result_zombie += len_zombie - len_plants  # Добавляем оставшийся элементы в случае если массив Зомби был больше.

    if result_plants > result_zombie:
        return True                           #  True -> Если победа Растений.
    elif result_zombie > result_plants:
        return False                          #  False -> Если победа Зомби.
    else:
        if result_plants == result_zombie:    #  Если выживших одинаковое число, вернет True если начальная сила Растений больше.
            return sum_power_plants == sum_power_zombie  # вернет False если начальная сила Зомби больше.




def test_task():

    assert attack([ 1, 3, 4, 7], [ 2, 4, 6, 8 ]) == True
    assert attack([ 1, 3, 5, 7 ], [ 2, 4 ] ) == False
    assert attack([ 1, 3, 5, 7 ], [ 2, 4, 0, 8 ]) == True
    assert attack([ 2, 1, 1, 1 ], [ 1, 2, 1, 1 ]) == True

    print("All tests passed!")

test_task()








