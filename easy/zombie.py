

def attack(zombies:list[int], plants:list[int]) -> bool:

    '''
    Функция принимает два массива чисел, zombie and plants ,
    возвращает True -> если plants победил,
    возвращает False -> если zombie победил
    '''

    sum_power_plants = sum(plants)
    sum_power_zombie = sum(zombies)

    len_plants = len(plants)
    len_zombie = len(zombies)

    result_plants = 0
    result_zombie = 0

    for plant, zombie in zip(plants, zombies):
        if plant > zombie:
            result_plants += 1
        elif zombie > plant:
            result_zombie += 1
    result_plants += len_plants - len_zombie
    result_zombie += len_zombie - len_plants

    if result_plants > result_zombie:
        return True
    elif result_zombie > result_plants:
        return False
    else:
        if result_plants == result_zombie:
            return sum_power_plants > sum_power_zombie



print( attack(plants=[2,4,6], zombies=[1, 3, 5, 6]))







