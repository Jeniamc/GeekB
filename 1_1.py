### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час
# <m> мин <s> сек.

duration = int(input('Введите  промежутк времени в секундах:'))
duration_f = (duration // (60 * 24 * 60))
duration_d = (duration // (60 * 60) - 24 * duration_f)
duration_b = (duration // 60 % 60)
duration_a = duration % 60
print('Ответ:', duration_f, 'дн', duration_d, 'час', duration_b, 'мин', duration_a, 'сек')
