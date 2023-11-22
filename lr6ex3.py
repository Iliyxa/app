
from random import *

class N_ERROR(Exception):
    pass

while True:
  try:
      n = int(input('Введите целое число N, количество элементов -> '))
      if n < 2:
        raise N_ERROR
      break
  except ValueError:
    print('Ошибка, введено не целое число')
  except N_ERROR:
    print('Ошибка, N < 2, минимум должно быть 2 элемента')

mas = [ randint(-100,100) for _ in range(n)]
print(mas)
index = -1
summa_odd = 0
summa = 0
first_index = -1
last_index = -1

for i in range(0,len(mas),2):
    summa_odd += mas[i]
print(f'Сумма элементов списка с нечетными номерами {summa_odd}')

for i in range(len(mas)):
    if mas[i] < 0:
        first_index = i
        break
for i in range(len(mas)):
    if mas[i] < 0:
        last_index = i
if first_index != -1 or last_index != -1:
    for i in range(first_index, last_index+1):
        summa += mas[i]
else:
    summa = 0
print(f'Сумма элементов списка, расположенных между первым и последним отрицательными элементами {summa}')
