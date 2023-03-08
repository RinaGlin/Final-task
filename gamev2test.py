""" Game: Guess the number"""
"The computer guesses number independently"

import numpy as np

def random_predict(number:int=1) -> int:                                    #Создаём функцию для угадывания числа.
    """Randomly guess a number

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0                                                              #Создаём счётчик попыток.
    low = 0                                                                #Задаём нижний предел для бинарной функции.
    high = 101                                                             #Задаём верхний предел для бинарной функции.
    mean = 1                                                               #Определяем начальное значение среднего значения между верхним и нижним значением пределами.
    while number != mean:                                                  #Задаём цикл, который работает, пока среднее значение не равно загаданному числу.
        count += 1
        mean = (low + high)//2                                             #Вычисляем среднее значение.
        if number > mean:
            low = mean                                                     #Если загаданное число больше среднего значения, то диапазон поиска смещается вправо.
        elif number < mean:
            high = mean                                                    #Если загаданное число меньше среднего значения, то диапазон поиска смещается влево от него.
 
    return(count) 

def score_game(random_predict) -> int:                                     #Создаём функцию для подсчёта попыток.
    """For how many attempts on average out of 1000 apporoaches your algorithm guesses

    Args:
        random_predict (_type_): guess function

    Returns:
        int: average numbers of attempts
    """
    count_ls = []                                                           #Создаём пустой список для подсчёта попыток.
    np.random.seed(1)                                                       #Фиксируем начальные условия для воспроизводимости кода.
    random_array = np.random.randint(1, 101, size=(1000))                   #Задаём множество значений.
    
    for number in random_array:                                             #Запускаем цикл для каждого значения из множества.
        count_ls.append(random_predict(number))                             #Добавляем количество попыток в список подсчёта попыток.
    score = int(np.mean(count_ls))                                          #Считаем среднее значение списка попыток.
    
    print(f"Your algorithm guesses number on average on {score} attempts")  #Выводим на экран сообщение о числе попыток.
    
    return(score)                                                           #Завершаем функцию. 

if __name__ == '__main__':                                                  #Обозначаем модуль верхнего уровня.
    score_game(random_predict)                                              #Вывод на экран результата функции.
  