import numpy as np

water_height = np.array([4.01, 4.03, 4.27, 4.29, 4.19,
4.15, 4.16, 4.23, 4.29, 4.19,
4.00, 4.22, 4.25, 4.19, 4.10,
4.14, 4.03, 4.23, 4.08, 14.20,
14.03, 11.20, 8.19, 6.18, 4.04,
4.08, 4.11, 4.23, 3.99, 4.23])

# print(np.mean(water_height)) --среднее значение массива--
water_height_sorted = np.sort(water_height)
median_water_height = np.median(water_height) # --медиана массива-- 4.19
# Хотя медиана говорит нам, где находится середина наших данных, давайте посмотрим на
# значение ближе к концу набора данных. Мы можем использовать процентили, чтобы
# использовать позицию точек данных и получить ее значение:
np.percentile(water_height, 75)  # 75-й процентиль --4.265--
# Мы получили представление о значениях нашего набора данных. Но как насчет
# распространения наших данных? Давайте рассчитаем стандартное отклонение, чтобы
# понять, насколько похожи или насколько различны каждая из точек данных:
np.std(water_height)  # стандартное отклонение --2.784585367099861--

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18, 9, 2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])
store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)
# print(store_one_avg, store_two_avg, store_three_avg)  # 6.5 10.428571428571429 5.0
best_store = 'store_two' if store_two_avg > 7 else 'store_one' if store_one_avg > 7 else 'store_three'
# print(best_store)  # store_two


# Когда np.mean вычисляет логический оператор, результирующее среднее значение будет
# эквивалентно общему количеству элементов True, разделенному на общую длину массива.
# В нашем примере опроса продукции мы можем использовать этот расчет, чтобы узнать
# процент людей, которые покупали более 8 фунтов продукции каждую неделю:
# >>> np.mean(survey_array > 8)
# 0.2
# Логический оператор survey_array> 8 оценивает, какие ответы на опрос были больше 8, и
# присваивает им значение 1. np.mean складывает все единицы и делит их на длину массива
# survey_array. Полученные результаты говорят нам, что 20% респондентов купили более 8
# фунтов продукции.

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006
, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 
2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977
, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 
1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977
, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 
2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994
, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])
millenials = np.mean(class_year >= 2005)
# print(millenials)  # 0.21

# Во-первых, мы можем использовать np.mean, чтобы найти среднее значение по всем
# массивам:
# >>> ring_toss = np.array([[1, 0, 0],
# [0, 0, 1],
# [1, 0, 1]])
# >>> np.mean(ring_toss)
# .44444444444444442
# Чтобы найти среднее каждого внутреннего массива, мы указываем ось 1 («строки»):
# >>> np.mean(ring_toss, axis=1)
# array([ 0.33333333, 0.33333333, 0.66666667])
# Чтобы найти среднее значение каждой позиции индекса (т.е. среднее значение всех
# первых бросков, среднее значение всех вторых бросков,…), мы указываем ось 0
# («столбцы»):
# >>> np.mean(ring_toss, axis=0)
# array([ 0.66666667, 0. , 0.66666667])

allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])
total_mean = np.mean(allergy_trials)
# print(total_mean)  # 5.0
trial_mean = np.mean(allergy_trials, axis=1)
# print(trial_mean)  # [4. 5.6 6.2]
patient_mean = np.mean(allergy_trials, axis=0)
# print(patient_mean)  # [4.33333333 3.         4.         8.66666667 6.33333333]
temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91,
97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93,
90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 
96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90,
98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])
sorted_temps = np.sort(temps)
# print(sorted_temps)
# [ 85  85  85  85  85  86  86  86  86  86  86  86  87  87  87  87  87  87
#   87  88  88  88  88  88  88  88  88  89  89  90  90  90  90  90  90  90
#   90  91  91  91  92  92  92  92  92  93  93  93  93  93  94  94  94  94
#   94  94  94  95  95  96  96  96  96  96  96  97  97  97  97  97  98  98
#   98  98  98  98  99  99  99  99  99 100 101 101 187 191 195 196 198 199]

# в NumPy также есть функция для вычисления
# медианы np.median:
# >>> my_array = np.array([50, 38, 291, 59, 14])
# >>> np.median(my_array)
# 50.0

income_list = [10100, 35500, 105000, 85000, 25500, 40500, 65000]
small_set_median = income_list[len(income_list) // 2]  # 85000

large_set = np.genfromtxt('home_income.csv', delimiter=None, invalid_raise=False)
large_set = large_set.flatten()
large_set_clean = large_set[~np.isnan(large_set)]
large_set_median = np.median(large_set_clean)
print(large_set_median)  # 91112.0

# >>> d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8])
# >>> np.percentile(d, 40)
# 4.00
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])
thirtieth_percentile = np.percentile(patrons, 30)
seventieth_percentile = np.percentile(patrons, 70)  
# print(thirtieth_percentile)  # 3.0
#print(seventieth_percentile)  # 8.0

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])
first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)
interquartile_range = third_quarter - first_quarter
# print(first_quarter)  # 1.0
# print(third_quarter)  # 3.5
# print(interquartile_range)  # 2.5

# Cтандартное отклонение говорит нам о разбросе
# данных. Чем больше стандартное отклонение, тем больше наши данные разбросаны от
# центра. Чем меньше стандартное отклонение, тем больше данные сгруппированы вокруг
# среднего значения.
# Мы можем найти стандартное отклонение набора данных с помощью функции Numpy
# np.std:
# >>> nums = np.array([65, 36, 52, 91, 63, 79])
# >>> np.std(nums)
# 17.716909687891082

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])
acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])
pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)
pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)
print(pumpkin_avg, acorn_squash_avg)  
print(pumpkin_std, acorn_squash_std)
winner = 'pumpkin' if pumpkin_std > acorn_squash_std else 'acorn_squash'
# print(winner)  # pumpkin

numpy_rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.36, 4.82, 5.11])
rain_mean = np.mean(numpy_rainfall)
rain_median = np.median(numpy_rainfall)
first_quarter = np.precentile(numpy_rainfall, 25)
third_quarter = np.percentile(numpy_rainfall, 75)
interquartile_range = third_quarter - first_quarter
rain_std = np.std(numpy_rainfall)
