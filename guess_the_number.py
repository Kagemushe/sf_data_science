import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict_number = np.random.randint(1, 101) #Предпологаемое число

    while count < 20: #Число попыток не должно превышать лимит (20 попыток)
        count += 1

        #Подбираем нужное нам число
        if number < predict_number:
          predict_number -= 1

        elif number > predict_number:
          predict_number += 1 

        else:
            break #Выход из цикла, если угадали
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов
    угадывает наш алгоритм
    
    Args:
         random_predict ([type]): функция угадывания
    
    Returns:
        int: среднее количество попыток
    """ 
    count_ls = [] #Список для сохранения количества попыток
    np.random.seed(1) #Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
    #Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #Находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)



    # Ваш код заканчивается здесь

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)