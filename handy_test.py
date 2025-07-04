import math # Импорт модуля math

def func(x):
    return math.log(math.log(x))

try:  
    result = func(1)
    print(result)
except(TypeError):
    print("Ошибка типов данных")
except(ValueError):
    print("Ошибка вычисления логарифма из отрицательного числа или нуля\единицы")
except Exception as e:
    print(f'Тип ошибки: {e}')

'''
1. Положительное число -> корректный ответ +
2. отрицательное число -> Ошибка вычисления логарифма из отрицательного числа или нуля\единицы +
3. 0 -> Ошибка вычисления логарифма из отрицательного числа или нуля\единицы +
4. 1 -> Ошибка вычисления логарифма из отрицательного числа или нуля\единицы +
5. текст -> Ошибка типов данных +
6. дробное число -> корректный ответ  + 
7. пустой ввод -> Ошибка типов данных +
'''