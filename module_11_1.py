import requests
import numpy
from matplotlib import pyplot as plt

print(f'Использование модуля - requests\n')
url = 'https://urban-university.ru'
response = requests.get(url)
print(f'Число, указывающее состояние HTTP-ответа {response.status_code}')
print(f'Кодировка для декодирования контента - {response.encoding}')
print(f'Текстовое представление ответа HTTP-статуса - {response.reason}')
print('Заголовкаи сервера, которые он вернул во время ответа')
for key, value in response.headers.items():
    print(f'{key}, --- {value}')
print()
print(f'Использование модуля - numpy\n')
array_ = numpy.array([1, 2, 3, 4, 5, 6, 7 ])
print(f'Одномерный массив NumPy - {array_}')
array_1 = numpy.array([[1, 2, 3], [4, 5, 6]])
print(f'Многомерный массив NumPy - \n {array_1}')
print(f'Количество измерений многомерного массива -  {array_1.ndim}')
print(f'Сумма всех элементов многомерного массива - {array_1.sum()}')
array_2 = numpy.zeros((3,3))
print(f'Массив numpy 3×3, где каждый элемент равен 0 - \n {array_2}')
array_3 = numpy.arange(5,25,4)
print(f'Массив numpy, элементы которого лежат в диапазоне значений \n от 5 до 25 с разницей равной 4 - \n {array_3}')
print()

print(f'Использование модуля - matplotlib')
x = ['1 квартал', '2 квартал', '3 квартал', '4 квартал']
y = [3, 5, 8, 7]
plt.bar(x, y, label='Величина прибыли')
plt.xlabel('Квартал года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Столбчатая диаграмма')
plt.legend()
plt.show()