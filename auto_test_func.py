import math

def func(x):
    return math.log(math.log(x))

def heand(x):
    try:  
        result = func(x)
        print(result)
    except(TypeError):
        result = "Ошибка типов данных"
        print("Ошибка типов данных")
    except(ValueError):
        result = "Ошибка вычисления логарифма из отрицательного числа или нуля"
        print("Ошибка вычисления логарифма из отрицательного числа или нуля")
    except Exception as e:
        result = 'Тип ошибки: {e}'
        print(f'Тип ошибки: {e}')
    return result